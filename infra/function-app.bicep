@description('The location for all resources')
param location string = resourceGroup().location

@description('The name of the function app')
param functionAppName string

@description('The name of the storage account for function runtime (3-24 chars, lowercase letters and numbers only)')
@minLength(3)
@maxLength(24)
param functionStorageAccountName string

@description('The name of the App Service Plan')
param appServicePlanName string = '${functionAppName}-plan'

@description('The SKU for the App Service Plan')
@allowed([
  'Y1'       // Consumption plan
  'EP1'      // Elastic Premium
  'EP2'
  'EP3'
])
param appServicePlanSku string = 'Y1'

@description('The name of the Application Insights instance')
param applicationInsightsName string = '${functionAppName}-insights'

@description('Enable Application Insights')
param enableApplicationInsights bool = true

@description('The FEC API key (stored in app settings)')
@secure()
param fecApiKey string

@description('The blob storage account URL for FEC filings data')
param blobAccountUrl string

@description('The blob container name for FEC filings data')
param blobContainerName string = 'fec-filings'

@description('User-assigned managed identity client ID (optional)')
param managedIdentityClientId string = ''

// Storage account for Azure Functions runtime
resource functionStorageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: functionStorageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
    allowBlobPublicAccess: false
    minimumTlsVersion: 'TLS1_2'
    supportsHttpsTrafficOnly: true
    encryption: {
      services: {
        blob: {
          enabled: true
          keyType: 'Account'
        }
        file: {
          enabled: true
          keyType: 'Account'
        }
        queue: {
          enabled: true
          keyType: 'Account'
        }
        table: {
          enabled: true
          keyType: 'Account'
        }
      }
      keySource: 'Microsoft.Storage'
    }
  }
}

// Application Insights for monitoring
resource applicationInsights 'Microsoft.Insights/components@2020-02-02' = if (enableApplicationInsights) {
  name: applicationInsightsName
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    Request_Source: 'rest'
    RetentionInDays: 90
  }
}

// App Service Plan (Consumption or Premium)
resource appServicePlan 'Microsoft.Web/serverfarms@2023-01-01' = {
  name: appServicePlanName
  location: location
  sku: {
    name: appServicePlanSku
    tier: appServicePlanSku == 'Y1' ? 'Dynamic' : 'ElasticPremium'
  }
  properties: {
    reserved: true // Required for Linux
  }
}

// Function App
resource functionApp 'Microsoft.Web/sites@2023-01-01' = {
  name: functionAppName
  location: location
  kind: 'functionapp,linux'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    serverFarmId: appServicePlan.id
    httpsOnly: true
    siteConfig: {
      linuxFxVersion: 'Python|3.11'
      pythonVersion: '3.11'
      ftpsState: 'Disabled'
      minTlsVersion: '1.2'
      http20Enabled: true
      appSettings: [
        {
          name: 'AzureWebJobsStorage'
          value: 'DefaultEndpointsProtocol=https;AccountName=${functionStorageAccount.name};EndpointSuffix=${environment().suffixes.storage};AccountKey=${functionStorageAccount.listKeys().keys[0].value}'
        }
        {
          name: 'WEBSITE_CONTENTAZUREFILECONNECTIONSTRING'
          value: 'DefaultEndpointsProtocol=https;AccountName=${functionStorageAccount.name};EndpointSuffix=${environment().suffixes.storage};AccountKey=${functionStorageAccount.listKeys().keys[0].value}'
        }
        {
          name: 'WEBSITE_CONTENTSHARE'
          value: toLower(functionAppName)
        }
        {
          name: 'FUNCTIONS_EXTENSION_VERSION'
          value: '~4'
        }
        {
          name: 'FUNCTIONS_WORKER_RUNTIME'
          value: 'python'
        }
        {
          name: 'APPLICATIONINSIGHTS_CONNECTION_STRING'
          value: enableApplicationInsights ? applicationInsights!.properties.ConnectionString : ''
        }
        {
          name: 'FEC_API_KEY'
          value: fecApiKey
        }
        {
          name: 'BLOB_ACCOUNT_URL'
          value: blobAccountUrl
        }
        {
          name: 'BLOB_CONTAINER_NAME'
          value: blobContainerName
        }
        {
          name: 'AZURE_CLIENT_ID'
          value: managedIdentityClientId
        }
      ]
    }
  }
}

@description('The resource ID of the function app')
output functionAppId string = functionApp.id

@description('The name of the function app')
output functionAppName string = functionApp.name

@description('The default hostname of the function app')
output functionAppHostname string = functionApp.properties.defaultHostName

@description('The principal ID of the function app managed identity')
output functionAppPrincipalId string = functionApp.identity.principalId

@description('The resource ID of the function storage account')
output functionStorageAccountId string = functionStorageAccount.id

@description('The resource ID of Application Insights')
output applicationInsightsId string = enableApplicationInsights ? applicationInsights!.id : ''

@description('The instrumentation key of Application Insights')
output applicationInsightsInstrumentationKey string = enableApplicationInsights ? applicationInsights!.properties.InstrumentationKey : ''
