# Deployment Guide

This guide covers local development and Azure deployment for the FEC Data Sync project.

## Prerequisites

| Tool                          | Purpose                      | Installation                             |
| ----------------------------- | ---------------------------- | ---------------------------------------- |
| Python 3.11+                  | Runtime                      | [python.org][python]                     |
| uv                            | Package manager              | [docs.astral.sh/uv][uv]                  |
| Azure CLI                     | Azure management             | [Install Azure CLI][az-cli]              |
| Azure Functions Core Tools v4 | Local function development   | [Install Core Tools][az-func-tools]      |
| Azurite                       | Local storage emulator       | `npm install -g azurite` ([docs][azurite]) |
| FEC API Key                   | Data source access           | [api.open.fec.gov][fec-api]              |

## Local Development

### 1. Install Dependencies

```bash
make install
```

### 2. Start Local Storage Emulator

```bash
make azurite-start
```

This starts [Azurite][azurite] and creates the required blob container (`fec-filings`).

### 3. Configure Local Settings

Copy the example settings file and add your FEC API key:

```bash
cp apps/data-sync/local.settings.json.example apps/data-sync/local.settings.json
```

Edit `local.settings.json`:

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "FEC_API_KEY": "<your-fec-api-key>",
    "BLOB_ACCOUNT_URL": "http://127.0.0.1:10000/devstoreaccount1",
    "BLOB_CONTAINER_NAME": "fec-filings"
  }
}
```

### 4. Run Function Apps

```bash
# Run data-sync function
make run-data-sync

# Or run email-update function
make run-email-update
```

### 5. Trigger Functions Manually

**Data-sync function:**

```bash
# Trigger manual sync
curl -X POST http://localhost:7071/api/sync
```

**Email-update function** (run on port 7072 or stop data-sync first):

```bash
# Preview email for a committee
curl http://localhost:7071/api/preview/{committee_id}

# Send test email
curl -X POST http://localhost:7071/api/send-test-email/{committee_id}
```

### 6. Run Tests

```bash
make test
```

### 7. Stop Emulator

```bash
make azurite-stop
```

---

## Azure Deployment

### Option 1: Using Make Commands (Recommended)

The simplest way to deploy is using the provided Makefile commands.

#### First-Time Setup

```bash
# 1. Login to Azure
make az-login

# 2. Create resource group
make az-create-rg

# 3. Register Azure providers (one-time only)
make az-register-providers
```

#### Deploy Everything

```bash
# Set your FEC API key
export FEC_API_KEY=your-fec-api-key

# Deploy infrastructure and all function apps
make deploy-all
```

#### Deploy Individually

```bash
# Infrastructure only
make deploy-infra

# Function apps (after infrastructure is deployed)
make deploy-data-sync
make deploy-email-update
```

#### Custom Configuration

Override defaults with environment variables:

```bash
export AZURE_RESOURCE_GROUP=my-resource-group
export AZURE_LOCATION=westus2
export ENVIRONMENT=prod
export FEC_API_KEY=your-key

make deploy-all
```

| Variable               | Default            | Description                             |
| ---------------------- | ------------------ | --------------------------------------- |
| `AZURE_RESOURCE_GROUP` | `fec-data-sync-rg` | Resource group name                     |
| `AZURE_LOCATION`       | `eastus`           | [Azure region][az-regions]              |
| `ENVIRONMENT`          | `dev`              | Environment: `dev`, `staging`, `prod`   |
| `FEC_API_KEY`          | -                  | Your FEC API key (required)             |

---

### Option 2: GitHub Actions

The project includes a GitHub Actions workflow for CI/CD.

#### Setup OIDC Authentication

1. Create an Azure AD app registration:

```bash
# Create app registration
az ad app create --display-name "github-fec-data-sync"

# Get the app ID
APP_ID=$(az ad app list --display-name "github-fec-data-sync" --query "[0].appId" -o tsv)

# Create service principal
az ad sp create --id $APP_ID

# Get subscription ID
SUBSCRIPTION_ID=$(az account show --query id -o tsv)

# Assign Contributor role
az role assignment create \
  --assignee $APP_ID \
  --role Contributor \
  --scope /subscriptions/$SUBSCRIPTION_ID/resourceGroups/fec-data-sync-rg

# Configure federated credentials for GitHub
az ad app federated-credential create \
  --id $APP_ID \
  --parameters '{
    "name": "github-main",
    "issuer": "https://token.actions.githubusercontent.com",
    "subject": "repo:<your-org>/<your-repo>:ref:refs/heads/main",
    "audiences": ["api://AzureADTokenExchange"]
  }'
```

See [Configuring OpenID Connect in Azure][az-oidc] for more details.

2. Configure GitHub repository secrets:

| Secret                  | Description                 |
| ----------------------- | --------------------------- |
| `AZURE_CLIENT_ID`       | App registration client ID  |
| `AZURE_TENANT_ID`       | Azure AD tenant ID          |
| `AZURE_SUBSCRIPTION_ID` | Azure subscription ID       |
| `FEC_API_KEY`           | FEC API key                 |

3. Configure GitHub repository variables:

| Variable               | Description         |
| ---------------------- | ------------------- |
| `AZURE_RESOURCE_GROUP` | Resource group name |

#### Triggering Deployment

- **Automatic**: Push to `main` branch
- **Manual**: Actions > Deploy to Azure > Run workflow

---

### Option 3: Manual Azure CLI

For full control, use Azure CLI directly.

#### Deploy Infrastructure

```bash
az deployment group create \
  --resource-group fec-data-sync-rg \
  --template-file infra/main.bicep \
  --parameters environment=dev \
  --parameters fecApiKey=<your-fec-api-key>
```

#### Deploy Function Code

```bash
# Build the package
make build-data-sync

# Deploy to Azure
cd apps/data-sync
func azure functionapp publish data-sync-dev
```

See [Deployment technologies in Azure Functions][az-func-deploy] for more options.

---

## Monitoring

### Application Insights

The deployment creates [Application Insights][az-app-insights] with a [Log Analytics Workspace][az-log-analytics] for monitoring.

**Access in Azure Portal:**
1. Navigate to your Resource Group
2. Select the Application Insights resource (`<app-name>-insights`)

### Viewing Logs

```bash
# Stream logs in real-time
func azure functionapp logstream <function-app-name>

# Or via Azure CLI
az webapp log tail --name <function-app-name> --resource-group <resource-group>
```

### Key Metrics

| Metric                   | Description                              |
| ------------------------ | ---------------------------------------- |
| Function execution count | Number of trigger executions             |
| Function duration        | Execution time per invocation            |
| Failures                 | Failed executions                        |
| Dependencies             | External calls (Blob Storage, FEC API)   |

See [Monitor Azure Functions][az-func-monitor] for more details.

---

## Environment Variables

| Variable                  | Description                      | Required |
| ------------------------- | -------------------------------- | -------- |
| `FEC_API_KEY`             | FEC API authentication key       | Yes      |
| `BLOB_ACCOUNT_URL`        | Azure Blob Storage account URL   | Yes      |
| `BLOB_CONTAINER_NAME`     | Container name for storing files | Yes      |
| `AZURE_CLIENT_ID`         | Managed identity client ID       | No       |
| `EMAIL_CONNECTION_STRING` | ACS connection string            | Auto     |
| `EMAIL_SENDER_ADDRESS`    | Sender email address             | Auto     |
| `AZURE_OPENAI_ENDPOINT`   | OpenAI endpoint URL              | Auto     |

Variables marked "Auto" are automatically configured during deployment.

---

## Troubleshooting

### Function not triggering

- Check Application Insights for errors
- Verify timer trigger schedule in `function_app.py`
- Ensure `AzureWebJobsStorage` is configured correctly
- See [Timer trigger troubleshooting][az-func-timer]

### Blob storage access denied

- Verify managed identity role assignment completed
- Check `BLOB_ACCOUNT_URL` is correct
- For local dev, ensure Azurite is running
- See [Managed identity authentication][az-func-identity]

### FEC API errors

- Verify `FEC_API_KEY` is valid
- Check FEC API rate limits (1,000 requests/hour)
- See [FEC API documentation][fec-api]

### Useful Commands

```bash
# View function app settings
az functionapp config appsettings list \
  --name <app-name> \
  --resource-group <rg>

# Restart function app
az functionapp restart \
  --name <app-name> \
  --resource-group <rg>

# View deployment status
az deployment group show \
  --name main \
  --resource-group <rg>
```

---

## Make Commands Reference

| Command                    | Description                      |
| -------------------------- | -------------------------------- |
| `make install`             | Install all dependencies         |
| `make lint`                | Run linting and type checks      |
| `make test`                | Run tests                        |
| `make azurite-start`       | Start local storage emulator     |
| `make azurite-stop`        | Stop local storage emulator      |
| `make run-data-sync`       | Run data-sync function locally   |
| `make run-email-update`    | Run email-update function locally|
| `make build-functions`     | Build all function packages      |
| `make deploy-infra`        | Deploy Azure infrastructure      |
| `make deploy-data-sync`    | Deploy data-sync function        |
| `make deploy-email-update` | Deploy email-update function     |
| `make deploy-all`          | Deploy everything                |
| `make az-login`            | Login to Azure CLI               |
| `make az-create-rg`        | Create resource group            |
| `make az-register-providers`| Register Azure providers        |
| `make clean`               | Remove generated files           |

---

## FEC Form Types and Report Types Reference

### Form Types

FEC forms determine the structure of financial reports. Each form type has different data fields and is used by different types of committees.

#### ✅ Supported Forms

| Form | Committee Type |
|------|----------------|
| **F3** | House & Senate Candidate Committees |

#### All Form Types

| Form | Committee Type |
|------|----------------|
| F3 | House & Senate Candidate Committees |
| F3P | Presidential Candidate Committees |
| F3X | PACs, Super PACs, and Party Committees |
| F3L | Bundled Contributions |
| F4 | Convention Committees |
| F5 | Independent Expenditures |
| F6 | 48-Hour Notice of Contributions |
| F7 | Communication Costs |
| F9 | Electioneering Communications |
| F13 | Inaugural Committee Donations |

### Report Types

Report types indicate the filing period.

#### ✅ Supported Report Types

| Code | Description | Coverage Period |
|------|-------------|-----------------|
| **Q1** | April Quarterly | January 1 - March 31 |
| **Q2** | July Quarterly | April 1 - June 30 |
| **Q3** | October Quarterly | July 1 - September 30 |
| **YE** | Year-End | October 1 - December 31 |

#### All Report Types

**Quarterly**
| Code | Description |
|------|-------------|
| Q1 | April Quarterly |
| Q2 | July Quarterly |
| Q3 | October Quarterly |
| YE | Year-End |
| Q2S | July Quarterly / Semi-Annual |
| QYE | Quarterly Semi-Annual (Year-End) |

**Monthly**
| Code | Description |
|------|-------------|
| M2 | February Monthly |
| M3 | March Monthly |
| M4 | April Monthly |
| M5 | May Monthly |
| M6 | June Monthly |
| M7 | July Monthly |
| M8 | August Monthly |
| M9 | September Monthly |
| M10 | October Monthly |
| M11 | November Monthly |
| M12 | December Monthly |
| MSA | Monthly Semi-Annual (Mid-Year) |

**Election**
| Code | Description |
|------|-------------|
| 12P | Pre-Primary (12 days before) |
| 12G | Pre-General (12 days before) |
| 30P | Post-Primary (30 days after) |
| 30G | Post-General (30 days after) |
| 30R | Post-Runoff (30 days after) |
| 30S | Post-Special (30 days after) |

**Other**
| Code | Description |
|------|-------------|
| 48 | 48-Hour Report of Independent Expenditures |
| TER | Termination Report |

---

<!-- Reference Links - Official Documentation -->
[python]: https://www.python.org/downloads/
[uv]: https://docs.astral.sh/uv/getting-started/installation/
[az-cli]: https://learn.microsoft.com/cli/azure/install-azure-cli
[az-func-tools]: https://learn.microsoft.com/azure/azure-functions/functions-run-local
[azurite]: https://learn.microsoft.com/azure/storage/common/storage-use-azurite
[fec-api]: https://api.open.fec.gov/developers/
[az-regions]: https://azure.microsoft.com/explore/global-infrastructure/geographies
[az-oidc]: https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-azure
[az-func-deploy]: https://learn.microsoft.com/azure/azure-functions/functions-deployment-technologies
[az-app-insights]: https://learn.microsoft.com/azure/azure-monitor/app/app-insights-overview
[az-log-analytics]: https://learn.microsoft.com/azure/azure-monitor/logs/log-analytics-overview
[az-func-monitor]: https://learn.microsoft.com/azure/azure-functions/functions-monitoring
[az-func-timer]: https://learn.microsoft.com/azure/azure-functions/functions-bindings-timer
[az-func-identity]: https://learn.microsoft.com/azure/azure-functions/functions-identity-based-connections-tutorial
