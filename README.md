# Copilot Agent Prototype - FEC Update Emailer

A prototype application that syncs Federal Election Commission (FEC) filings data to Azure Blob Storage and sends email notifications with AI-generated summaries when new filings are detected.

## 📦 Project Structure

```
├── apps/
│   ├── data-sync/              # Azure Function for syncing FEC data
│   └── email-update/           # Azure Function for email notifications
├── packages/
│   ├── fec-api-client/         # Generated FEC API client library
│   └── services/               # Shared services
│       ├── email.py            # Azure Communication Services email
│       ├── file_sync.py        # FEC data synchronization
│       ├── storage.py          # Azure Blob Storage operations
│       ├── summary.py          # Azure OpenAI summary generation
│       └── templates.py        # Email HTML templates
├── infra/                      # Bicep templates for Azure infrastructure
└── docs/                       # Documentation
    ├── deployment.md           # Deployment guide
    └── infrastructure.md       # Infrastructure details
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- [uv][uv] package manager
- Azure CLI (for deployment)
- Azure Functions Core Tools (for local development)
- [Azurite][azurite] (for local storage emulation)

### Installation

```bash
make install
```

## 🛠️ Development

This project uses a Makefile for common development tasks:

| Command                | Description                              |
| ---------------------- | ---------------------------------------- |
| `make install`         | Install all dependencies                 |
| `make lint`            | Run ruff formatter, linter, and ty       |
| `make test`            | Run tests                                |
| `make azurite-start`   | Start Azurite (Azure Storage emulator)   |
| `make azurite-stop`    | Stop Azurite                             |
| `make run-data-sync`   | Run data-sync function locally           |
| `make run-email-update`| Run email-update function locally        |
| `make clean`           | Remove generated files                   |

### Running Locally

1. Start the Azure Storage emulator:
   ```bash
   make azurite-start
   ```

2. Run either function app:
   ```bash
   make run-data-sync
   # or
   make run-email-update
   ```

## 🏗️ Architecture

### Azure Services

| Service                       | Purpose                                        |
| ----------------------------- | ---------------------------------------------- |
| Azure Functions               | Serverless compute for data sync and email     |
| Azure Blob Storage            | Storage for FEC filings data and manifests     |
| Azure Communication Services  | Email delivery                                 |
| Azure OpenAI                  | AI-generated summaries of new filings          |
| Azure Application Insights    | Monitoring and diagnostics                     |
| Azure Managed Identity        | Secure authentication between services         |

### External APIs

| API     | Purpose                                 |
| ------- | --------------------------------------- |
| FEC API | Federal Election Commission data source |

## 📚 Documentation

- [Deployment Guide][docs-deployment]
- [Infrastructure Details][docs-infrastructure]

## 📄 License

See [LICENSE][license] for details.

<!-- Reference Links -->
[uv]: https://docs.astral.sh/uv/
[azurite]: https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite
[docs-deployment]: ./docs/deployment.md
[docs-infrastructure]: ./docs/infrastructure.md
[license]: ./LICENSE
