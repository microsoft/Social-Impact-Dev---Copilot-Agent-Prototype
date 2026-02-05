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

@description('Enable email update function app')
param enableEmailFunction bool = false

// Generate unique suffix for globally unique names
var uniqueSuffix = uniqueString(resourceGroup().id)
var storageAccountName = toLower(replace('${baseName}${environment}${uniqueSuffix}', '-', ''))
var functionStorageAccountName = toLower(replace('${baseName}func${uniqueSuffix}', '-', ''))
var functionAppName = '${baseName}-${environment}'
var emailFunctionAppName = 'email-update-${environment}'
var emailFunctionStorageAccountName = toLower(replace('emailfunc${uniqueSuffix}', '-', ''))
var containerName = 'fec-filings'
var manifestContainerName = 'manifests'

// Storage account for FEC filings data
module storage 'storage.bicep' = {
  name: 'storage-deployment'
  params: {
    location: location
    storageAccountName: take(storageAccountName, 24) // Max 24 chars
    containerName: containerName
    storageSku: 'Standard_LRS'
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
  }
}

// Azure Communication Services for email (only if email function enabled)
module communicationServices 'communication-services.bicep' = if (enableEmailFunction) {
  name: 'communication-services-deployment'
  params: {
    communicationServicesName: '${baseName}-${environment}-acs'
    dataLocation: 'United States'
  }
}

// Azure OpenAI for summaries (only if email function enabled)
module openAI 'openai.bicep' = if (enableEmailFunction) {
  name: 'openai-deployment'
  params: {
    location: location
    openAIName: '${baseName}-${environment}-openai'
    modelName: openAIModel
    deploymentName: openAIModel
  }
}

// Function app with Application Insights
module functionApp 'function-app.bicep' = {
  name: 'function-app-deployment'
  params: {
    location: location
    functionAppName: functionAppName
    functionStorageAccountName: take(functionStorageAccountName, 24) // Max 24 chars
    appServicePlanSku: appServicePlanSku
    enableApplicationInsights: enableApplicationInsights
    logRetentionDays: logRetentionDays
    fecApiKey: fecApiKey
    blobAccountUrl: storage.outputs.accountUrl
    blobContainerName: containerName
  }
}

// Role assignment for function app to access storage
module roleAssignment 'role-assignment.bicep' = {
  name: 'role-assignment-deployment'
  params: {
    principalId: functionApp.outputs.functionAppPrincipalId
    storageAccountId: storage.outputs.storageAccountId
    roleName: 'Storage Blob Data Contributor'
  }
}

// Manifest storage container for email triggers
module manifestStorage 'storage.bicep' = if (enableEmailFunction) {
  name: 'manifest-storage-deployment'
  params: {
    location: location
    storageAccountName: take(storageAccountName, 24) // Use same storage account
    containerName: manifestContainerName
    storageSku: 'Standard_LRS'
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
  }
  dependsOn: [storage]
}

// Reference deployed resources to get secrets (only when email function enabled)
resource storageAccountRef 'Microsoft.Storage/storageAccounts@2023-01-01' existing = if (enableEmailFunction) {
  name: storage.outputs.storageAccountName
}

resource acsRef 'Microsoft.Communication/communicationServices@2023-04-01' existing = if (enableEmailFunction) {
  name: communicationServices.outputs.communicationServicesName
}

resource openAIRef 'Microsoft.CognitiveServices/accounts@2024-10-01' existing = if (enableEmailFunction) {
  name: openAI.outputs.openAIName
}

// Email update function app
module emailFunctionApp 'email-function-app.bicep' = if (enableEmailFunction) {
  name: 'email-function-app-deployment'
  params: {
    location: location
    functionAppName: emailFunctionAppName
    functionStorageAccountName: take(emailFunctionStorageAccountName, 24)
    appServicePlanSku: appServicePlanSku
    enableApplicationInsights: enableApplicationInsights
    logRetentionDays: logRetentionDays
    blobConnectionString: 'DefaultEndpointsProtocol=https;AccountName=${storageAccountRef.name};EndpointSuffix=${az.environment().suffixes.storage};AccountKey=${storageAccountRef.listKeys().keys[0].value}'
    blobAccountUrl: storage.outputs.accountUrl
    blobContainerName: containerName
    manifestContainerName: manifestContainerName
    // Use auto-generated values if not provided manually
    emailConnectionString: !empty(emailConnectionString) ? emailConnectionString : acsRef.listKeys().primaryConnectionString
    emailSenderAddress: !empty(emailSenderAddress) ? emailSenderAddress : communicationServices.outputs.senderAddress
    emailRecipientList: emailRecipientList
    azureOpenAIEndpoint: !empty(azureOpenAIEndpoint) ? azureOpenAIEndpoint : openAI.outputs.endpoint
    azureOpenAIApiKey: !empty(azureOpenAIApiKey) ? azureOpenAIApiKey : openAIRef.listKeys().key1
    azureOpenAIDeployment: !empty(azureOpenAIDeployment) ? azureOpenAIDeployment : openAI.outputs.deploymentName
  }
}

// Role assignment for email function app to access storage
module emailRoleAssignment 'role-assignment.bicep' = if (enableEmailFunction) {
  name: 'email-role-assignment-deployment'
  params: {
    principalId: enableEmailFunction ? emailFunctionApp.outputs.functionAppPrincipalId : ''
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
output emailFunctionAppName string = enableEmailFunction ? emailFunctionApp.outputs.functionAppName : ''

@description('The email function app hostname')
output emailFunctionAppHostname string = enableEmailFunction ? emailFunctionApp.outputs.functionAppHostname : ''

@description('The auto-generated email sender address')
output emailSenderAddress string = enableEmailFunction ? communicationServices.outputs.senderAddress : ''

@description('The email domain')
output emailDomain string = enableEmailFunction ? communicationServices.outputs.emailDomain : ''

@description('The Azure OpenAI endpoint')
output azureOpenAIEndpoint string = enableEmailFunction ? openAI.outputs.endpoint : ''

@description('The Azure OpenAI deployment name')
output azureOpenAIDeployment string = enableEmailFunction ? openAI.outputs.deploymentName : ''
