# Azure Infrastructure

This directory contains Bicep templates for deploying Azure resources.

## Files

- `storage.bicep` - Azure Storage Account and Blob Container for FEC filings data
- `function-app.bicep` - Azure Functions app for FEC data sync
- `role-assignment.bicep` - Role assignment module for granting storage access
- `*.parameters.json` - Example parameters files

## Deployment

### Prerequisites

- Azure CLI installed
- Logged in to Azure (`az login`)
- Target resource group created

### 1. Deploy Storage Account

```bash
# Create a resource group (if needed)
az group create --name <resource-group-name> --location <location>

# Deploy the storage account for FEC filings data
az deployment group create \
  --resource-group <resource-group-name> \
  --template-file infra/storage.bicep \
  --parameters storageAccountName=<unique-storage-name> \
  --parameters containerName=fec-filings
```

### 2. Deploy Function App

```bash
# Deploy the function app
az deployment group create \
  --resource-group <resource-group-name> \
  --template-file infra/function-app.bicep \
  --parameters functionAppName=fec-data-sync \
  --parameters functionStorageAccountName=<unique-func-storage-name> \
  --parameters fecApiKey=<your-fec-api-key> \
  --parameters blobAccountUrl=https://<storage-account>.blob.core.windows.net \
  --parameters blobContainerName=fec-filings
```

### 3. Grant Function App Access to Storage

After deploying both resources, grant the function app's managed identity access to the data storage:

```bash
# Get the function app's principal ID
PRINCIPAL_ID=$(az deployment group show \
  --resource-group <resource-group-name> \
  --name function-app \
  --query properties.outputs.functionAppPrincipalId.value -o tsv)

# Get the storage account ID
STORAGE_ID=$(az deployment group show \
  --resource-group <resource-group-name> \
  --name storage \
  --query properties.outputs.storageAccountId.value -o tsv)

# Deploy the role assignment
az deployment group create \
  --resource-group <resource-group-name> \
  --template-file infra/role-assignment.bicep \
  --parameters principalId=$PRINCIPAL_ID \
  --parameters storageAccountId=$STORAGE_ID \
  --parameters roleName="Storage Blob Data Contributor"
```

### Using Parameters Files

For production deployments, use parameters files:

```bash
# Deploy storage
az deployment group create \
  --resource-group <resource-group-name> \
  --template-file infra/storage.bicep \
  --parameters @infra/storage.parameters.json

# Deploy function app (update parameters file first)
az deployment group create \
  --resource-group <resource-group-name> \
  --template-file infra/function-app.bicep \
  --parameters @infra/function-app.parameters.json
```

## Resources Created

### Storage Account (`storage.bicep`)

- **Storage Account** - Azure Storage V2 account with:
  - Hot access tier
  - TLS 1.2+ enforcement
  - HTTPS only traffic
  - Encryption at rest
  - 7-day soft delete for blobs and containers

- **Blob Container** - Private blob container for FEC filings

### Function App (`function-app.bicep`)

- **Storage Account** - Dedicated storage for Azure Functions runtime
- **App Service Plan** - Consumption plan (Y1) by default
- **Function App** - Python 3.11 Linux function app with:
  - System-assigned managed identity
  - Application Insights integration
  - Configured environment variables for FEC sync
- **Application Insights** - Monitoring and diagnostics

## Outputs

### Storage Account

| Output | Description |
|--------|-------------|
| `accountUrl` | Blob endpoint URL (for `BLOB_ACCOUNT_URL`) |
| `containerName` | Container name (for `BLOB_CONTAINER_NAME`) |
| `storageAccountId` | Full resource ID |
| `storageAccountName` | Storage account name |

### Function App

| Output | Description |
|--------|-------------|
| `functionAppId` | Full resource ID |
| `functionAppName` | Function app name |
| `functionAppHostname` | Default hostname |
| `functionAppPrincipalId` | Managed identity principal ID |
| `applicationInsightsId` | Application Insights resource ID |

## Environment Variables

The function app is configured with these environment variables:

| Variable | Description |
|----------|-------------|
| `FEC_API_KEY` | FEC API authentication key |
| `BLOB_ACCOUNT_URL` | Azure Blob Storage account URL |
| `BLOB_CONTAINER_NAME` | Container name for storing files |
| `AZURE_CLIENT_ID` | (Optional) User-assigned managed identity client ID |

## Deploying Function Code

After infrastructure deployment, deploy the function code:

```bash
cd apps/fec-data-sync

# Install Azure Functions Core Tools if needed
# brew install azure-functions-core-tools@4

# Deploy to Azure
func azure functionapp publish <function-app-name>
```
