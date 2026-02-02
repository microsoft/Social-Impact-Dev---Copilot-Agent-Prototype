# Copilot Agent Prototype - FEC Update Emailer

A prototype application that syncs Federal Election Commission (FEC) filings data to Azure Blob Storage using Azure Functions.

## 📦 Project Structure

```
├── apps/
│   └── fec-data-sync/       # Azure Functions app for syncing FEC data
├── packages/
│   ├── fec-api-client/      # Generated FEC API client library
│   └── services/            # Shared services (FileSyncService, AzureBlobStorageService)
└── infra/                   # Bicep templates for Azure infrastructure
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager
- Azure CLI (for deployment)
- Azure Functions Core Tools (for local development)

### Installation

```bash
# Install dependencies (including dev tools)
uv sync --dev
```

## 🛠️ Development Commands

| Command                       | Description                          |
| ----------------------------- | ------------------------------------ |
| `uv sync --dev`               | Install all dependencies             |
| `uv run ruff check .`         | Run linter                           |
| `uv run ruff check . --fix`   | Run linter with auto-fix             |
| `uv run ruff format .`        | Format code                          |
| `uv run ruff format . --check`| Check formatting without changes     |
| `uv run ty check .`           | Run type checker                     |
| `uv run pytest`               | Run tests                            |
| `uv run pytest -v`            | Run tests with verbose output        |

## 🏗️ Architecture

### Microsoft Products & Services

| Service                     | Purpose                                       |
| --------------------------- | --------------------------------------------- |
| Azure Functions             | Serverless compute for scheduled FEC data sync|
| Azure Blob Storage          | Storage for FEC filings data                  |
| Azure Application Insights  | Monitoring and diagnostics                    |
| Azure Managed Identity      | Secure authentication between services        |

### External APIs

| API     | Purpose                                |
| ------- | -------------------------------------- |
| FEC API | Federal Election Commission data source|

## 📚 Infrastructure

See [infra/README.md](./infra/README.md) for detailed deployment instructions.

## 📄 License

See [LICENSE](./LICENSE) for details.
