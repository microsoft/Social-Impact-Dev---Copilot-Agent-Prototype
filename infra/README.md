# Azure Storage Infrastructure

This directory contains Bicep templates for deploying Azure Storage resources.

## Files

- `storage.bicep` - Main Bicep template for Azure Storage Account and Blob Container
- `storage.parameters.json` - Example parameters file

## Deployment

### Prerequisites

- Azure CLI installed
- Logged in to Azure (`az login`)
- Target resource group created

### Deploy with Azure CLI

```bash
# Create a resource group (if needed)
az group create --name <resource-group-name> --location <location>

# Deploy the storage account
az deployment group create \
  --resource-group <resource-group-name> \
  --template-file infra/storage.bicep \
  --parameters storageAccountName=<unique-storage-name> \
  --parameters containerName=data

# Or use the parameters file
az deployment group create \
  --resource-group <resource-group-name> \
  --template-file infra/storage.bicep \
  --parameters infra/storage.parameters.json
```

### Get Deployment Outputs

```bash
az deployment group show \
  --resource-group <resource-group-name> \
  --name storage \
  --query properties.outputs
```

## Resources Created

1. **Storage Account** - Azure Storage V2 account with:
   - Hot access tier
   - TLS 1.2+ enforcement
   - HTTPS only traffic
   - Encryption at rest
   - 7-day soft delete for blobs and containers

2. **Blob Container** - Private blob container with no public access

## Outputs

The deployment provides the following outputs for use with `BlobStorageService`:

- `accountUrl` - The blob endpoint URL (for `BLOB_ACCOUNT_URL` env var)
- `containerName` - The name of the created container (for `BLOB_CONTAINER_NAME` env var)
- `storageAccountName` - The storage account name
- `storageAccountId` - The full resource ID

## Managed Identity Setup

After deployment, grant your managed identity access to the storage account:

```bash
# Get the storage account ID
STORAGE_ID=$(az deployment group show \
  --resource-group <resource-group-name> \
  --name storage \
  --query properties.outputs.storageAccountId.value -o tsv)

# Assign Storage Blob Data Contributor role to your managed identity
az role assignment create \
  --assignee <managed-identity-principal-id> \
  --role "Storage Blob Data Contributor" \
  --scope $STORAGE_ID
```
