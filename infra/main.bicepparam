using './main.bicep'

// Environment configuration
param environment = readEnvironmentVariable('ENVIRONMENT', 'dev')
param baseName = readEnvironmentVariable('BASE_NAME', 'data-sync')
param enableApplicationInsights = true
param logRetentionDays = 90

// FEC API configuration (required)
param fecApiKey = readEnvironmentVariable('FEC_API_KEY', '')
param fecCommitteeIds = readEnvironmentVariable('FEC_COMMITTEE_IDS', '')
param fecReportTypes = readEnvironmentVariable('FEC_REPORT_TYPES', '')

// Email configuration (optional)
param emailConnectionString = readEnvironmentVariable('EMAIL_CONNECTION_STRING', '')
param emailSenderAddress = readEnvironmentVariable('EMAIL_SENDER_ADDRESS', '')
param emailRecipientList = readEnvironmentVariable('EMAIL_RECIPIENT_LIST', '')

// Azure OpenAI configuration (optional)
param azureOpenAIEndpoint = readEnvironmentVariable('AZURE_OPENAI_ENDPOINT', '')
param azureOpenAIApiKey = readEnvironmentVariable('AZURE_OPENAI_API_KEY', '')
param azureOpenAIDeployment = readEnvironmentVariable('AZURE_OPENAI_DEPLOYMENT', '')
