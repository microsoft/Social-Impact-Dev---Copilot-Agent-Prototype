# FEC Data Sync

A prototype application that syncs Federal Election Commission (FEC) filings data to Azure and sends email notifications with AI-generated summaries when new filings are detected.

## Architecture

```mermaid
flowchart LR
    FEC["FEC API"] --> DS["data-sync<br/>Function App"]
    DS --> Blob["Azure Blob<br/>Storage"]
    Blob --> EU["email-update<br/>Function App"]
    EU --> OpenAI["Azure OpenAI"]
    EU --> ACS["Azure Communication<br/>Services"]
    ACS --> Email["Email Recipients"]
```

See [Infrastructure Documentation][docs-infra] for the complete architecture diagram and resource details.

## Quick Start

### Prerequisites

- Python 3.11+ ([python.org][python])
- [uv][uv] package manager
- [Azure Functions Core Tools][az-func-tools]
- [Azurite][azurite] (local storage emulator)
- [FEC API key][fec-api]

### Local Development

```bash
# Install dependencies
make install

# Start local storage emulator
make azurite-start

# Run a function app
make run-data-sync
```

### Deploy to Azure

```bash
# Login and setup
make az-login
make az-create-rg
make az-register-providers

# Deploy everything
export FEC_API_KEY=your-key
make deploy-all
```

## Project Structure

```
├── apps/
│   ├── data-sync/           # Syncs FEC data on a schedule
│   └── email-update/        # Sends email notifications on new filings
├── packages/
│   ├── fec-api-client/      # Generated FEC API client
│   └── services/            # Shared services (email, storage, AI)
├── infra/                   # Bicep templates for Azure
└── docs/                    # Documentation
```

## Make Commands

| Command                | Description                |
| ---------------------- | -------------------------- |
| `make install`         | Install dependencies       |
| `make test`            | Run tests                  |
| `make lint`            | Run linting                |
| `make azurite-start`   | Start local storage        |
| `make run-data-sync`   | Run data-sync locally      |
| `make run-email-update`| Run email-update locally   |
| `make deploy-all`      | Deploy to Azure            |
| `make help`            | Show all commands          |

## Documentation

- [Deployment Guide][docs-deploy] - Local development and Azure deployment
- [Infrastructure][docs-infra] - Azure resources and Bicep templates

## Azure Services Used

| Service                                  | Purpose                |
| ---------------------------------------- | ---------------------- |
| [Azure Functions][az-functions]          | Serverless compute     |
| [Azure Blob Storage][az-storage]         | FEC filings storage    |
| [Azure Communication Services][az-acs]   | Email delivery         |
| [Azure OpenAI][az-openai]                | AI-generated summaries |
| [Application Insights][az-app-insights]  | Monitoring             |

## License

See [LICENSE][license] for details.

<!-- Reference Links -->
[python]: https://www.python.org/downloads/
[uv]: https://docs.astral.sh/uv/
[az-func-tools]: https://learn.microsoft.com/azure/azure-functions/functions-run-local
[azurite]: https://learn.microsoft.com/azure/storage/common/storage-use-azurite
[fec-api]: https://api.open.fec.gov/developers/
[az-functions]: https://learn.microsoft.com/azure/azure-functions/functions-overview
[az-storage]: https://learn.microsoft.com/azure/storage/blobs/storage-blobs-introduction
[az-acs]: https://learn.microsoft.com/azure/communication-services/overview
[az-openai]: https://learn.microsoft.com/azure/ai-services/openai/overview
[az-app-insights]: https://learn.microsoft.com/azure/azure-monitor/app/app-insights-overview
[docs-deploy]: ./docs/deployment.md
[docs-infra]: ./docs/infrastructure.md
[license]: ./LICENSE
