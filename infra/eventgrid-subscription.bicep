@description('The Event Grid system topic name')
param eventGridTopicName string

@description('The email function app name')
param emailFunctionAppName string

@description('The blob container name')
param containerName string = 'fec-filings'

resource eventGridSystemTopic 'Microsoft.EventGrid/systemTopics@2024-06-01-preview' existing = {
  name: eventGridTopicName
}

resource emailFunctionApp 'Microsoft.Web/sites@2023-12-01' existing = {
  name: emailFunctionAppName
}

// Event Grid subscription to trigger email function on report.json creation
resource eventGridSubscription 'Microsoft.EventGrid/systemTopics/eventSubscriptions@2024-06-01-preview' = {
  parent: eventGridSystemTopic
  name: 'email-report-created'
  properties: {
    destination: {
      endpointType: 'AzureFunction'
      properties: {
        resourceId: '${emailFunctionApp.id}/functions/process_new_report'
        maxEventsPerBatch: 1
        preferredBatchSizeInKilobytes: 64
      }
    }
    filter: {
      includedEventTypes: [
        'Microsoft.Storage.BlobCreated'
      ]
      subjectBeginsWith: '/blobServices/default/containers/${containerName}/blobs/'
      subjectEndsWith: '/report.json'
    }
    eventDeliverySchema: 'EventGridSchema'
  }
}

@description('The Event Grid subscription name')
output subscriptionName string = eventGridSubscription.name
