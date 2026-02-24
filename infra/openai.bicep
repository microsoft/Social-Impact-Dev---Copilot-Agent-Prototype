@description('The location for the Azure OpenAI resource')
param location string = resourceGroup().location

@description('The name of the Azure OpenAI resource')
param openAIName string

@description('The SKU for the Azure OpenAI resource')
@allowed([
  'S0'
])
param sku string = 'S0'

@description('The model to deploy')
@allowed([
  'gpt-4o'
  'gpt-4o-mini'
  'gpt-4'
  'gpt-35-turbo'
])
param modelName string = 'gpt-4o-mini'

@description('The model version')
param modelVersion string = '2024-07-18'

@description('The deployment name')
param deploymentName string = 'gpt-4o-mini'

@description('Tokens per minute capacity (in thousands)')
param capacityK int = 10

@description('Whether to deploy the model (set to false if deployment already exists)')
param deployModel bool = true

// Azure OpenAI resource
resource openAI 'Microsoft.CognitiveServices/accounts@2024-10-01' = {
  name: openAIName
  location: location
  kind: 'OpenAI'
  sku: {
    name: sku
  }
  properties: {
    customSubDomainName: openAIName
    publicNetworkAccess: 'Enabled'
  }
}

// Model deployment (conditional to avoid redeployment errors)
resource deployment 'Microsoft.CognitiveServices/accounts/deployments@2024-10-01' = if (deployModel) {
  parent: openAI
  name: deploymentName
  sku: {
    name: 'Standard'
    capacity: capacityK
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: modelName
      version: modelVersion
    }
  }
}

@description('The Azure OpenAI resource ID')
output openAIId string = openAI.id

@description('The Azure OpenAI resource name')
output openAIName string = openAI.name

@description('The Azure OpenAI endpoint')
output endpoint string = openAI.properties.endpoint

@description('The deployment name')
output deploymentName string = deployModel ? deployment.name : deploymentName
