using './main.bicep'

param environment = 'dev'
param baseName = 'data-sync'
param appServicePlanSku = 'Y1'
param enableApplicationInsights = true
param logRetentionDays = 90

// Required secret - set FEC_API_KEY environment variable before deploying
param fecApiKey = readEnvironmentVariable('FEC_API_KEY', '')
