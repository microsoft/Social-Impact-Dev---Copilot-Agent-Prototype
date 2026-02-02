@description('The principal ID to assign the role to')
param principalId string

@description('The principal type')
@allowed([
  'ServicePrincipal'
  'User'
  'Group'
])
param principalType string = 'ServicePrincipal'

@description('The resource ID of the storage account')
param storageAccountId string

@description('The role to assign')
@allowed([
  'Storage Blob Data Contributor'
  'Storage Blob Data Reader'
  'Storage Blob Data Owner'
])
param roleName string = 'Storage Blob Data Contributor'

// Built-in role definition IDs
var roleDefinitionIds = {
  'Storage Blob Data Contributor': 'ba92f5b4-2d11-453d-a403-e96b0029c9fe'
  'Storage Blob Data Reader': '2a2b9908-6ea1-4ae2-8e65-a410df84e7d1'
  'Storage Blob Data Owner': 'b7e6dc6d-f1e8-4753-8033-0f276bb0955b'
}

// Reference the existing storage account
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' existing = {
  name: last(split(storageAccountId, '/'))
}

// Role assignment
resource roleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(storageAccountId, principalId, roleDefinitionIds[roleName])
  scope: storageAccount
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', roleDefinitionIds[roleName])
    principalId: principalId
    principalType: principalType
  }
}

@description('The role assignment ID')
output roleAssignmentId string = roleAssignment.id
