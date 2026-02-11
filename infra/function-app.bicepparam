using './data-sync-app.bicep'

param functionAppName = 'fec-data-sync'
param functionStorageAccountName = 'fecdatasyncfunc'
param appServicePlanSku = 'Y1'
param blobAccountUrl = 'https://<storage-account>.blob.core.windows.net'
param blobContainerName = 'fec-filings'

// Required secret - set FEC_API_KEY environment variable before deploying
param fecApiKey = readEnvironmentVariable('FEC_API_KEY', '')
