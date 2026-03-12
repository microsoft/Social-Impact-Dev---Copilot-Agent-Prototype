# Prerequisites

This document outlines the requirements for deploying and running the FEC Data Sync solution.

## Azure Subscription

An active [Azure subscription](https://azure.microsoft.com/free/) is required. The solution uses consumption-based Azure services with pay-as-you-go pricing.

## Azure Services

The following Azure services are provisioned during deployment:

| Service | Purpose | Pricing |
|---------|---------|---------|
| [Azure Functions](https://learn.microsoft.com/azure/azure-functions/functions-overview) | Serverless compute for data sync and email functions | [Consumption plan](https://azure.microsoft.com/pricing/details/functions/) |
| [Azure Blob Storage](https://learn.microsoft.com/azure/storage/blobs/storage-blobs-introduction) | Storage for FEC filings and processed data | [Storage pricing](https://azure.microsoft.com/pricing/details/storage/blobs/) |
| [Azure Communication Services](https://learn.microsoft.com/azure/communication-services/overview) | Email delivery for notifications | [Email pricing](https://azure.microsoft.com/pricing/details/communication-services/) |
| [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/overview) | AI-generated summaries and analysis | [OpenAI pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) |
| [Application Insights](https://learn.microsoft.com/azure/azure-monitor/app/app-insights-overview) | Monitoring and logging | [Monitor pricing](https://azure.microsoft.com/pricing/details/monitor/) |

## External APIs

| API | Purpose | Access |
|-----|---------|--------|
| [FEC API](https://api.open.fec.gov/developers/) | Federal Election Commission filings data | Free API key required |

## Local Development Tools

For local development, see the [Deployment Guide](./deployment.md#prerequisites) for required tools (Python, Azure Functions Core Tools, etc.).

## Azure Resource Providers

The following Azure resource providers must be registered in your subscription. This is handled automatically by `make az-register-providers`:

- `Microsoft.Web` (Azure Functions)
- `Microsoft.Storage` (Blob Storage)
- `Microsoft.Communication` (Communication Services)
- `Microsoft.CognitiveServices` (Azure OpenAI)
- `Microsoft.Insights` (Application Insights)
- `Microsoft.EventGrid` (Event Grid triggers)

## Permissions

To deploy the solution, you need:

- **Contributor** role on the target resource group (or ability to create one)
- Ability to register resource providers (or have them pre-registered)
- Ability to create managed identities and role assignments

See the [Deployment Guide](./deployment.md) for detailed deployment instructions.
