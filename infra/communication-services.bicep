@description('The location for the Communication Services resource')
param location string = 'global' // ACS is a global service

@description('The name of the Communication Services resource')
param communicationServicesName string

@description('The location for the Email Communication Services resource')
param emailLocation string = 'global'

@description('Data location for email service')
@allowed([
  'United States'
  'Europe'
  'United Kingdom'
  'Australia'
  'Japan'
  'France'
  'Switzerland'
])
param dataLocation string = 'United States'

// Azure Communication Services resource
resource communicationServices 'Microsoft.Communication/communicationServices@2023-04-01' = {
  name: communicationServicesName
  location: location
  properties: {
    dataLocation: dataLocation
  }
}

// Email Communication Services resource
resource emailService 'Microsoft.Communication/emailServices@2023-04-01' = {
  name: '${communicationServicesName}-email'
  location: emailLocation
  properties: {
    dataLocation: dataLocation
  }
}

// Azure-managed email domain (auto-verified)
resource emailDomain 'Microsoft.Communication/emailServices/domains@2023-04-01' = {
  parent: emailService
  name: 'AzureManagedDomain'
  location: emailLocation
  properties: {
    domainManagement: 'AzureManaged'
    userEngagementTracking: 'Disabled'
  }
}

// Link email service to communication services
resource emailLink 'Microsoft.Communication/communicationServices/emailLinks@2023-04-01' = {
  parent: communicationServices
  name: 'default'
  properties: {
    linkedDomains: [
      emailDomain.id
    ]
  }
}

@description('The Communication Services resource ID')
output communicationServicesId string = communicationServices.id

@description('The Communication Services connection string')
output connectionString string = communicationServices.listKeys().primaryConnectionString

@description('The email sender address (DoNotReply)')
output senderAddress string = 'DoNotReply@${emailDomain.properties.mailFromSenderDomain}'

@description('The email domain')
output emailDomain string = emailDomain.properties.mailFromSenderDomain
