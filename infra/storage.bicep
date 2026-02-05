@description('The location for all resources')
param location string = resourceGroup().location

@description('The name of the storage account (3-24 chars, lowercase letters and numbers only)')
@minLength(3)
@maxLength(24)
param storageAccountName string

@description('The name of the blob container')
param containerName string = 'fec-filings'

@description('The SKU for the storage account')
@allowed([
  'Standard_LRS'
  'Standard_GRS'
  'Standard_RAGRS'
  'Standard_ZRS'
  'Premium_LRS'
  'Premium_ZRS'
])
param storageSku string = 'Standard_LRS'

@description('Enable hierarchical namespace (Data Lake Gen2)')
param enableHierarchicalNamespace bool = false

@description('Minimum TLS version')
@allowed([
  'TLS1_2'
  'TLS1_3'
])
param minimumTlsVersion string = 'TLS1_2'

@description('Allow public access to blobs')
param allowBlobPublicAccess bool = false

@description('Container public access level')
@allowed([
  'None'
  'Blob'
  'Container'
])
param containerPublicAccess string = 'None'

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: storageSku
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
    allowBlobPublicAccess: allowBlobPublicAccess
    minimumTlsVersion: minimumTlsVersion
    supportsHttpsTrafficOnly: true
    isHnsEnabled: enableHierarchicalNamespace
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
      }
      keySource: 'Microsoft.Storage'
    }
    networkAcls: {
      defaultAction: 'Allow'
      bypass: 'AzureServices'
    }
  }
}

resource blobService 'Microsoft.Storage/storageAccounts/blobServices@2023-01-01' = {
  parent: storageAccount
  name: 'default'
  properties: {
    deleteRetentionPolicy: {
      enabled: true
      days: 7
    }
    containerDeleteRetentionPolicy: {
      enabled: true
      days: 7
    }
  }
}

resource container 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = {
  parent: blobService
  name: containerName
  properties: {
    publicAccess: containerPublicAccess
  }
}

@description('The resource ID of the storage account')
output storageAccountId string = storageAccount.id

@description('The name of the storage account')
output storageAccountName string = storageAccount.name

@description('The primary blob endpoint URL')
output blobEndpoint string = storageAccount.properties.primaryEndpoints.blob

@description('The blob account URL for use with BlobStorageService')
output accountUrl string = storageAccount.properties.primaryEndpoints.blob

@description('The name of the blob container')
output containerName string = container.name
