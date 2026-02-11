@description('The location for all resources')
param location string = resourceGroup().location

@description('Environment name (used for resource naming)')
@allowed([
  'dev'
  'staging'
  'prod'
])
param environment string = 'dev'

@description('Base name for resources')
param baseName string = 'data-sync'

@description('The FEC API key (stored in app settings)')
@secure()
param fecApiKey string

@description('The SKU for the App Service Plan')
@allowed([
  'Y1'       // Consumption plan
  'EP1'      // Elastic Premium
  'EP2'
  'EP3'
])
param appServicePlanSku string = 'Y1'

@description('Enable Application Insights')
param enableApplicationInsights bool = true

@description('Log retention in days')
@minValue(30)
@maxValue(730)
param logRetentionDays int = 90

@description('Azure Communication Services connection string for email (auto-generated if not provided)')
@secure()
param emailConnectionString string = ''

@description('Email sender address (auto-generated if not provided)')
param emailSenderAddress string = ''

@description('Comma-separated list of email recipients')
param emailRecipientList string = ''

@description('Azure OpenAI endpoint (auto-generated if not provided)')
param azureOpenAIEndpoint string = ''

@description('Azure OpenAI API key (auto-generated if not provided)')
@secure()
param azureOpenAIApiKey string = ''

@description('Azure OpenAI deployment name (auto-generated if not provided)')
param azureOpenAIDeployment string = ''

@description('Azure OpenAI model to deploy')
@allowed([
  'gpt-4o'
  'gpt-4o-mini'
  'gpt-4'
  'gpt-35-turbo'
])
param openAIModel string = 'gpt-4o-mini'

@description('Enable role assignments (requires Owner or User Access Administrator role)')
param enableRoleAssignments bool = true

@description('Comma-separated list of FEC committee IDs to monitor (e.g., C00718866)')
param fecCommitteeIds string = ''

@description('Comma-separated list of FEC report/form types to filter (optional, e.g., F3,F3P,F3X)')
param fecReportTypes string = ''

// Generate unique suffix for globally unique names
var uniqueSuffix = uniqueString(resourceGroup().id)
var shortSuffix = take(uniqueSuffix, 6)
var storageAccountName = toLower(replace('${baseName}${environment}${uniqueSuffix}', '-', ''))
var functionStorageAccountName = toLower(replace('${baseName}func${uniqueSuffix}', '-', ''))
var functionAppName = '${baseName}-${environment}-${shortSuffix}'
var emailFunctionAppName = 'email-update-${environment}-${shortSuffix}'
var emailFunctionStorageAccountName = toLower(replace('emailfunc${uniqueSuffix}', '-', ''))
var containerName = 'fec-filings'
var manifestContainerName = 'manifests'

// Storage account for FEC filings data
module storage 'storage.bicep' = {
  name: 'storage-deployment'
  params: {
    location: location
    #disable-next-line BCP334
    storageAccountName: take(storageAccountName, 24)
    containerName: containerName
    storageSku: 'Standard_LRS'
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
  }
}

// Azure Communication Services for email
module communicationServices 'communication-services.bicep' = {
  name: 'communication-services-deployment'
  params: {
    communicationServicesName: 'email-update-${environment}-acs'
    dataLocation: 'United States'
  }
}

// Azure OpenAI for summaries
module openAI 'openai.bicep' = {
  name: 'openai-deployment'
  params: {
    location: location
    openAIName: 'email-update-${environment}-openai'
    modelName: openAIModel
    deploymentName: openAIModel
  }
}

// Function app with Application Insights
module functionApp 'data-sync-app.bicep' = {
  name: 'function-app-deployment'
  params: {
    location: location
    functionAppName: functionAppName
    #disable-next-line BCP334
    functionStorageAccountName: take(functionStorageAccountName, 24)
    appServicePlanSku: appServicePlanSku
    enableApplicationInsights: enableApplicationInsights
    logRetentionDays: logRetentionDays
    fecApiKey: fecApiKey
    blobAccountUrl: storage.outputs.accountUrl
    blobContainerName: containerName
    fecCommitteeIds: fecCommitteeIds
    fecReportTypes: fecReportTypes
  }
}

// Role assignment for function app to access storage
module roleAssignment 'role-assignment.bicep' = if (enableRoleAssignments) {
  name: 'role-assignment-deployment'
  params: {
    principalId: functionApp.outputs.functionAppPrincipalId
    storageAccountId: storage.outputs.storageAccountId
    roleName: 'Storage Blob Data Contributor'
  }
}

// Manifest storage container for email triggers
module manifestStorage 'storage.bicep' = {
  name: 'manifest-storage-deployment'
  params: {
    location: location
    #disable-next-line BCP334
    storageAccountName: take(storageAccountName, 24)
    containerName: manifestContainerName
    storageSku: 'Standard_LRS'
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
  }
  dependsOn: [storage]
}

// Reference deployed resources to get secrets
resource storageAccountRef 'Microsoft.Storage/storageAccounts@2023-01-01' existing = {
  #disable-next-line BCP334
  name: take(storageAccountName, 24)
  dependsOn: [storage]
}

resource acsRef 'Microsoft.Communication/communicationServices@2023-04-01' existing = {
  name: 'email-update-${environment}-acs'
  dependsOn: [communicationServices]
}

resource openAIRef 'Microsoft.CognitiveServices/accounts@2024-10-01' existing = {
  name: 'email-update-${environment}-openai'
  dependsOn: [openAI]
}

// Email update function app
module emailFunctionApp 'email-update-app.bicep' = {
  name: 'email-function-app-deployment'
  params: {
    location: location
    functionAppName: emailFunctionAppName
    #disable-next-line BCP334
    functionStorageAccountName: take(emailFunctionStorageAccountName, 24)
    appServicePlanSku: appServicePlanSku
    enableApplicationInsights: enableApplicationInsights
    logRetentionDays: logRetentionDays
    blobConnectionString: 'DefaultEndpointsProtocol=https;AccountName=${storageAccountRef.name};EndpointSuffix=${az.environment().suffixes.storage};AccountKey=${storageAccountRef.listKeys().keys[0].value}'
    blobAccountUrl: storage.outputs.accountUrl
    blobContainerName: containerName
    manifestContainerName: manifestContainerName
    emailConnectionString: !empty(emailConnectionString) ? emailConnectionString : acsRef.listKeys().primaryConnectionString
    emailSenderAddress: !empty(emailSenderAddress) ? emailSenderAddress : communicationServices.outputs.senderAddress
    emailRecipientList: emailRecipientList
    azureOpenAIEndpoint: !empty(azureOpenAIEndpoint) ? azureOpenAIEndpoint : openAI.outputs.endpoint
    azureOpenAIApiKey: !empty(azureOpenAIApiKey) ? azureOpenAIApiKey : openAIRef.listKeys().key1
    azureOpenAIDeployment: !empty(azureOpenAIDeployment) ? azureOpenAIDeployment : openAI.outputs.deploymentName
    fecCommitteeIds: fecCommitteeIds
  }
}

// Role assignment for email function app to access storage
module emailRoleAssignment 'role-assignment.bicep' = if (enableRoleAssignments) {
  name: 'email-role-assignment-deployment'
  params: {
    principalId: emailFunctionApp.outputs.functionAppPrincipalId
    storageAccountId: storage.outputs.storageAccountId
    roleName: 'Storage Blob Data Contributor'
  }
}

// Outputs
@description('The name of the data storage account')
output storageAccountName string = storage.outputs.storageAccountName

@description('The blob storage account URL')
output blobAccountUrl string = storage.outputs.accountUrl

@description('The blob container name')
output containerName string = storage.outputs.containerName

@description('The function app name')
output functionAppName string = functionApp.outputs.functionAppName

@description('The function app hostname')
output functionAppHostname string = functionApp.outputs.functionAppHostname

@description('The function app principal ID (managed identity)')
output functionAppPrincipalId string = functionApp.outputs.functionAppPrincipalId

@description('The Application Insights instrumentation key')
output applicationInsightsInstrumentationKey string = functionApp.outputs.applicationInsightsInstrumentationKey

@description('The Log Analytics Workspace ID')
output logAnalyticsWorkspaceId string = functionApp.outputs.logAnalyticsWorkspaceId

@description('The email function app name')
output emailFunctionAppName string = emailFunctionApp.outputs.functionAppName

@description('The email function app hostname')
output emailFunctionAppHostname string = emailFunctionApp.outputs.functionAppHostname

@description('The auto-generated email sender address')
output emailSenderAddress string = communicationServices.outputs.senderAddress

@description('The email domain')
output emailDomain string = communicationServices.outputs.emailDomain

@description('The Azure OpenAI endpoint')
output azureOpenAIEndpoint string = openAI.outputs.endpoint

@description('The Azure OpenAI deployment name')
output azureOpenAIDeployment string = openAI.outputs.deploymentName
