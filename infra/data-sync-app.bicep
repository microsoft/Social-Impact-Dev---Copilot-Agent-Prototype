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

@description('Comma-separated list of FEC committee IDs to monitor (e.g., C00718866)')
param fecCommitteeIds string = ''

@description('Comma-separated list of FEC report/form types to filter (optional, e.g., F3,F3P,F3X)')
param fecReportTypes string = ''

@description('The name of the Log Analytics Workspace')
param logAnalyticsWorkspaceName string = '${functionAppName}-logs'

@description('Log Analytics Workspace retention in days')
@minValue(30)
@maxValue(730)
param logRetentionDays int = 90

// Log Analytics Workspace for Application Insights
resource logAnalyticsWorkspace 'Microsoft.OperationalInsights/workspaces@2023-09-01' = if (enableApplicationInsights) {
  name: logAnalyticsWorkspaceName
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: logRetentionDays
    features: {
      enableLogAccessUsingOnlyResourcePermissions: true
    }
    workspaceCapping: {
      dailyQuotaGb: -1 // No cap
    }
  }
}

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

// Application Insights for monitoring (workspace-based)
resource applicationInsights 'Microsoft.Insights/components@2020-02-02' = if (enableApplicationInsights) {
  name: applicationInsightsName
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    Request_Source: 'rest'
    RetentionInDays: logRetentionDays
    WorkspaceResourceId: logAnalyticsWorkspace.id
    IngestionMode: 'LogAnalytics'
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
        {
          name: 'FEC_COMMITTEE_IDS'
          value: fecCommitteeIds
        }
        {
          name: 'FEC_REPORT_TYPES'
          value: fecReportTypes
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

@description('The resource ID of Log Analytics Workspace')
output logAnalyticsWorkspaceId string = enableApplicationInsights ? logAnalyticsWorkspace!.id : ''
