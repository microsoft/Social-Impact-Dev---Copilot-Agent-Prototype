# Azure Infrastructure

This document describes the Bicep templates for deploying Azure resources.

## Files

| File | Description |
|------|-------------|
| `main.bicep` | Main orchestration template - deploys all resources |
| `main.parameters.json` | Example parameters file for main.bicep |
| `storage.bicep` | Azure Storage Account and Blob Container |
| `function-app.bicep` | Azure Functions app with Application Insights |
| `role-assignment.bicep` | Role assignment for managed identity access |

## Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                        main.bicep                              │
│  Orchestrates deployment of all resources                      │
└───────────┬────────────────────┬───────────────────┬───────────┘
            │                    │                   │
            ▼                    ▼                   ▼
┌───────────────────┐  ┌─────────────────┐  ┌────────────────────┐
│   storage.bicep   │  │ function-app.   │  │ role-assignment.   │
│                   │  │     bicep       │  │       bicep        │
│ • Storage Account │  │ • Function App  │  │ • RBAC assignment  │
│ • Blob Container  │  │ • App Service   │  │   (Blob Data       │
│   (fec-filings)   │  │   Plan          │  │    Contributor)    │
│                   │  │ • App Insights  │  │                    │
│                   │  │ • Log Analytics │  │                    │
│                   │  │ • Func Storage  │  │                    │
└───────────────────┘  └─────────────────┘  └────────────────────┘
```

## Resources Created

### Storage Account (`storage.bicep`)

- **Storage Account (StorageV2)**
  - Hot access tier
  - TLS 1.2+ enforcement
  - HTTPS only traffic
  - Encryption at rest
  - 7-day soft delete for blobs and containers

- **Blob Container** - Private container for FEC filings

### Function App (`function-app.bicep`)

- **Log Analytics Workspace** - Centralized logging
- **Application Insights** - Monitoring and diagnostics (workspace-based)
- **Storage Account** - Dedicated storage for Azure Functions runtime
- **App Service Plan** - Consumption (Y1) or Elastic Premium (EP1-3)
- **Function App** - Python 3.11 Linux function app with:
  - System-assigned managed identity
  - Application Insights integration
  - Configured environment variables

### Role Assignment (`role-assignment.bicep`)

- **RBAC Role Assignment** - Grants function app access to blob storage
- Supports: `Storage Blob Data Contributor`, `Reader`, or `Owner`

## Deployment

### Using main.bicep (Recommended)

Deploy all resources with a single command:

```bash
az deployment group create \
  --resource-group <resource-group-name> \
  --template-file infra/main.bicep \
  --parameters environment=dev \
  --parameters fecApiKey=<your-fec-api-key>
```

### Using Parameters File

```bash
# First, update main.parameters.json with your values
az deployment group create \
  --resource-group <resource-group-name> \
  --template-file infra/main.bicep \
  --parameters @infra/main.parameters.json
```

### Deploying Individual Modules

For more control, deploy each module separately:

**1. Storage Account:**
```bash
az deployment group create \
  --resource-group <resource-group-name> \
  --template-file infra/storage.bicep \
  --parameters storageAccountName=<unique-name> \
  --parameters containerName=fec-filings
```

**2. Function App:**
```bash
az deployment group create \
  --resource-group <resource-group-name> \
  --template-file infra/function-app.bicep \
  --parameters functionAppName=fec-data-sync \
  --parameters functionStorageAccountName=<unique-name> \
  --parameters fecApiKey=<your-api-key> \
  --parameters blobAccountUrl=https://<storage>.blob.core.windows.net
```

**3. Role Assignment:**
```bash
az deployment group create \
  --resource-group <resource-group-name> \
  --template-file infra/role-assignment.bicep \
  --parameters principalId=<function-app-principal-id> \
  --parameters storageAccountId=<storage-account-id>
```

## Parameters

### main.bicep

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `location` | string | Resource group location | Azure region |
| `environment` | string | `dev` | Environment: `dev`, `staging`, `prod` |
| `baseName` | string | `fec-data-sync` | Base name for resources |
| `fecApiKey` | securestring | - | FEC API key (required) |
| `appServicePlanSku` | string | `Y1` | App Service Plan SKU |
| `enableApplicationInsights` | bool | `true` | Enable monitoring |
| `logRetentionDays` | int | `90` | Log retention period |

### function-app.bicep

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `functionAppName` | string | - | Function app name (required) |
| `functionStorageAccountName` | string | - | Storage for Functions runtime |
| `appServicePlanName` | string | `<name>-plan` | App Service Plan name |
| `appServicePlanSku` | string | `Y1` | SKU: Y1, EP1, EP2, EP3 |
| `applicationInsightsName` | string | `<name>-insights` | App Insights name |
| `enableApplicationInsights` | bool | `true` | Enable App Insights |
| `logAnalyticsWorkspaceName` | string | `<name>-logs` | Log Analytics name |
| `logRetentionDays` | int | `90` | Log retention (30-730 days) |
| `fecApiKey` | securestring | - | FEC API key (required) |
| `blobAccountUrl` | string | - | Blob storage URL (required) |
| `blobContainerName` | string | `fec-filings` | Container name |
| `managedIdentityClientId` | string | `` | User-assigned identity ID |

## Outputs

### main.bicep

| Output | Description |
|--------|-------------|
| `storageAccountName` | Data storage account name |
| `blobAccountUrl` | Blob storage URL |
| `containerName` | Blob container name |
| `functionAppName` | Function app name |
| `functionAppHostname` | Function app URL |
| `functionAppPrincipalId` | Managed identity principal ID |
| `applicationInsightsInstrumentationKey` | App Insights key |
| `logAnalyticsWorkspaceId` | Log Analytics workspace ID |

### function-app.bicep

| Output | Description |
|--------|-------------|
| `functionAppId` | Function app resource ID |
| `functionAppName` | Function app name |
| `functionAppHostname` | Default hostname |
| `functionAppPrincipalId` | Managed identity principal ID |
| `functionStorageAccountId` | Functions storage account ID |
| `applicationInsightsId` | App Insights resource ID |
| `applicationInsightsInstrumentationKey` | Instrumentation key |
| `logAnalyticsWorkspaceId` | Log Analytics workspace ID |

## Security

- All storage accounts enforce TLS 1.2+
- HTTPS-only traffic
- Blob public access disabled by default
- Managed identity for blob storage access (no connection strings)
- FEC API key stored as app setting (consider Key Vault for production)
- FTPS disabled on Function App
