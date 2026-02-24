# FEC Data Sync & Email Update

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

## Configuration

### Committee IDs

The `FEC_COMMITTEE_IDS` environment variable specifies which FEC committees to monitor. Committee IDs are unique identifiers assigned by the FEC, starting with "C" followed by 8 digits.

```bash
# Single committee
export FEC_COMMITTEE_IDS="C00703975"

# Multiple committees (comma-separated)
export FEC_COMMITTEE_IDS="C00703975,C00618371,C00401224"
```

You can find committee IDs on the [FEC website][fec-committees] by searching for a committee name.

#### Setting Committee IDs in Azure

After deploying to Azure, you can update the committee IDs directly in the Azure Portal:

1. Navigate to the [Azure Portal](https://portal.azure.com)
2. Go to your **Resource Group** (e.g., `rg-fec-data-sync-dev`)
3. Select the **data-sync** Function App (e.g., `data-sync-dev-xxxxxx`)
4. In the left menu, go to **Settings** → **Environment variables**
5. Find `FEC_COMMITTEE_IDS` and click to edit, or click **+ Add** if it doesn't exist
6. Enter your comma-separated committee IDs (e.g., `C00703975,C00618371`)
7. Click **Apply** and then **Confirm** to save changes

The function app will automatically restart with the new configuration.

For more details on managing Azure Functions environment variables, see [Configure app settings][az-func-app-settings].

### Report Types

The `FEC_REPORT_TYPES` environment variable filters which types of filings to sync. Currently, only quarterly reports are supported:

| Code | Description |
|------|-------------|
| `Q1` | April Quarterly (Jan 1 - Mar 31) |
| `Q2` | July Quarterly (Apr 1 - Jun 30) |
| `Q3` | October Quarterly (Jul 1 - Sep 30) |
| `YE` | Year-End (Oct 1 - Dec 31) |

```bash
export FEC_REPORT_TYPES="Q1,Q2,Q3,YE"
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
[fec-committees]: https://www.fec.gov/data/committees/
[az-func-app-settings]: https://learn.microsoft.com/azure/azure-functions/functions-how-to-use-azure-function-app-settings
