# Deployment Guide

This guide covers local development setup and Azure deployment for the FEC Data Sync project.

## Local Development

### Prerequisites

- Python 3.11+
- [uv][uv] package manager
- [Azure Functions Core Tools v4][azure-func-tools]
- [Azurite][azurite] (local storage emulator)
- FEC API key from [api.open.fec.gov][fec-api]

### Setup

1. **Install dependencies** from the workspace root:

   ```bash
   uv sync --dev
   ```

2. **Create local settings** for each function app:

   ```bash
   cd apps/fec-data-sync
   cp local.settings.json.example local.settings.json
   ```

3. **Configure local.settings.json**:

   ```json
   {
     "IsEncrypted": false,
     "Values": {
       "AzureWebJobsStorage": "UseDevelopmentStorage=true",
       "FUNCTIONS_WORKER_RUNTIME": "python",
       "FEC_API_KEY": "<your-fec-api-key>",
       "BLOB_ACCOUNT_URL": "http://127.0.0.1:10000/devstoreaccount1",
       "BLOB_CONTAINER_NAME": "fec-filings",
       "AZURE_STORAGE_CONNECTION_STRING": "UseDevelopmentStorage=true"
     }
   }
   ```

### Running Locally

1. **Start Azurite** (local storage emulator):

   ```bash
   # Install if needed: npm install -g azurite
   azurite --silent --location /tmp/azurite --debug /tmp/azurite/debug.log
   ```

2. **Create the blob container** (first time only):

   ```bash
   az storage container create \
     --name fec-filings \
     --connection-string "UseDevelopmentStorage=true"
   ```

3. **Start a function app**:

   ```bash
   cd apps/fec-data-sync
   func start
   ```

4. **Trigger timer functions manually** (for testing):

   ```bash
   curl -X POST http://localhost:7071/admin/functions/check_for_updates \
     -H "Content-Type: application/json" \
     -d '{}'
   ```

### Running Tests

```bash
uv run pytest
```

---

## Azure Deployment

### Option 1: GitHub Actions (Recommended)

The project includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) for automated deployment.

#### Prerequisites

1. **Create an Azure Resource Group**:

   ```bash
   az group create --name fec-data-sync-rg --location eastus
   ```

2. **Configure GitHub OIDC authentication**:

   Create an Azure AD app registration for GitHub Actions:

   ```bash
   # Create app registration
   az ad app create --display-name "github-fec-data-sync"

   # Get the app ID
   APP_ID=$(az ad app list --display-name "github-fec-data-sync" --query "[0].appId" -o tsv)

   # Create service principal
   az ad sp create --id $APP_ID

   # Get subscription ID
   SUBSCRIPTION_ID=$(az account show --query id -o tsv)

   # Assign Contributor role to resource group
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

3. **Configure GitHub secrets and variables**:

   **Secrets** (Settings > Secrets and variables > Actions > Secrets):
   | Secret | Description |
   |--------|-------------|
   | `AZURE_CLIENT_ID` | App registration client ID |
   | `AZURE_TENANT_ID` | Azure AD tenant ID |
   | `AZURE_SUBSCRIPTION_ID` | Azure subscription ID |
   | `FEC_API_KEY` | FEC API key |

   **Variables** (Settings > Secrets and variables > Actions > Variables):
   | Variable | Description |
   |----------|-------------|
   | `AZURE_RESOURCE_GROUP` | Resource group name (e.g., `fec-data-sync-rg`) |

4. **Create GitHub environment** (optional but recommended):

   Go to Settings > Environments > New environment > `dev`

#### Triggering Deployment

- **Automatic**: Push to `main` branch
- **Manual**: Actions > Deploy to Azure > Run workflow

---

### Option 2: Manual Deployment with Azure CLI

#### Deploy Infrastructure

```bash
# Login to Azure
az login

# Create resource group
az group create --name fec-data-sync-rg --location eastus

# Deploy all resources using main.bicep
az deployment group create \
  --resource-group fec-data-sync-rg \
  --template-file infra/main.bicep \
  --parameters environment=dev \
  --parameters fecApiKey=<your-fec-api-key>
```

#### Deploy Function Code

```bash
cd apps/fec-data-sync

# Build the package with dependencies
uv export --no-hashes -o requirements.txt
pip install --target .python_packages/lib/site-packages -r requirements.txt

# Copy workspace packages
cp -r ../../packages/fec-api-client/src/fec_api_client .python_packages/lib/site-packages/
cp -r ../../packages/services/src/services .python_packages/lib/site-packages/

# Deploy to Azure
func azure functionapp publish fec-data-sync-dev
```

---

## Monitoring

### Application Insights

The deployment creates Application Insights with a Log Analytics Workspace for comprehensive monitoring.

**Access via Azure Portal:**
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

| Metric | Description |
|--------|-------------|
| Function execution count | Number of trigger executions |
| Function duration | Execution time per invocation |
| Failures | Failed executions |
| Dependencies | External calls (Blob Storage, FEC API) |

---

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `FEC_API_KEY` | FEC API authentication key | Yes |
| `BLOB_ACCOUNT_URL` | Azure Blob Storage account URL | Yes |
| `BLOB_CONTAINER_NAME` | Container name for storing files | Yes |
| `AZURE_CLIENT_ID` | Managed identity client ID (user-assigned) | No |
| `AZURE_STORAGE_CONNECTION_STRING` | Storage connection string (local dev) | No |

---

## Troubleshooting

### Common Issues

**Function not triggering:**
- Check Application Insights for errors
- Verify the timer trigger schedule in `function_app.py`
- Ensure `AzureWebJobsStorage` is configured correctly

**Blob storage access denied:**
- Verify the managed identity role assignment completed
- Check `BLOB_ACCOUNT_URL` is correct
- For local dev, ensure Azurite is running

**FEC API errors:**
- Verify `FEC_API_KEY` is valid
- Check FEC API rate limits (1,000 requests/hour)

### Useful Commands

```bash
# View function app settings
az functionapp config appsettings list --name <app-name> --resource-group <rg>

# Restart function app
az functionapp restart --name <app-name> --resource-group <rg>

# View deployment status
az deployment group show --name main --resource-group <rg>
```

<!-- Reference Links -->
[uv]: https://docs.astral.sh/uv/
[azure-func-tools]: https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local
[azurite]: https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azurite
[fec-api]: https://api.open.fec.gov/developers/
