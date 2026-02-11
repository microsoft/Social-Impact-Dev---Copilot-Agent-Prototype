.PHONY: help install lint test build azurite-start azurite-stop run-data-sync run-email-update clean az-register-providers build-data-sync build-email-update build-functions deploy-infra deploy-data-sync deploy-email-update deploy-all demo

VENV_PATH := $(shell pwd)/.venv/bin
AZURITE_CONN := DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;

# Deployment configuration (override with environment variables)
AZURE_RESOURCE_GROUP ?= fec-data-sync-rg
AZURE_LOCATION ?= eastus
ENVIRONMENT ?= dev
BASE_NAME ?= data-sync

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Development:"
	@echo "  install              Install all dependencies"
	@echo "  lint                 Run linting and type checks"
	@echo "  test                 Run tests"
	@echo ""
	@echo "Local Testing:"
	@echo "  demo                 Run demo data sync (requires local.settings.json)"
	@echo "  azurite-start        Start Azurite (Azure Storage emulator)"
	@echo "  azurite-stop         Stop Azurite"
	@echo "  run-data-sync        Run data-sync function locally"
	@echo "  run-email-update     Run email-update function locally"
	@echo ""
	@echo "Build:"
	@echo "  build-functions      Build all function packages for deployment"
	@echo "  build-data-sync      Build data-sync function package"
	@echo "  build-email-update   Build email-update function package"
	@echo ""
	@echo "Deployment:"
	@echo "  deploy-infra         Deploy Azure infrastructure (Bicep)"
	@echo "  deploy-data-sync     Deploy data-sync function app code"
	@echo "  deploy-email-update  Deploy email-update function app code"
	@echo "  deploy-all           Deploy infrastructure and all function apps"
	@echo ""
	@echo "Azure Setup:"
	@echo "  az-login             Login to Azure CLI"
	@echo "  az-create-rg         Create Azure resource group"
	@echo "  az-register-providers Register required Azure resource providers"
	@echo ""
	@echo "Cleanup:"
	@echo "  clean                Remove generated files"
	@echo ""
	@echo "Configuration (environment variables):"
	@echo "  AZURE_RESOURCE_GROUP  Resource group name (default: fec-data-sync-rg)"
	@echo "  AZURE_LOCATION        Azure region (default: eastus)"
	@echo "  ENVIRONMENT           Environment name: dev|staging|prod (default: dev)"
	@echo "  FEC_API_KEY           FEC API key (required for deployment)"

install:
	uv sync --dev

lint:
	uv run ruff format .
	uv run ruff check .
	uv run ty check .

test:
	uv run pytest

# Start Azurite in background
azurite-start:
	@echo "Starting Azurite..."
	@pkill -f azurite 2>/dev/null || true
	@azurite --silent --skipApiVersionCheck --location /tmp/azurite &
	@sleep 2
	@echo "Creating containers..."
	@uv run python -c "\
from azure.storage.blob import BlobServiceClient; \
client = BlobServiceClient.from_connection_string('$(AZURITE_CONN)'); \
[client.create_container(c) for c in ['manifests', 'fec-filings'] if c not in [x.name for x in client.list_containers()]]" 2>/dev/null || true
	@echo "Azurite ready at http://127.0.0.1:10000"

azurite-stop:
	@pkill -f azurite 2>/dev/null || true
	@echo "Azurite stopped"

# Demo: sync FEC committee quarterly reports
demo:
	@echo "=== FEC Data Sync Demo ==="
	@# Start Azurite if not running
	@pgrep -f azurite > /dev/null || (echo "Starting Azurite..." && make azurite-start)
	@# Require existing local.settings.json
	@if [ ! -f apps/data-sync/local.settings.json ]; then \
		echo "Error: apps/data-sync/local.settings.json not found."; \
		echo "Copy from local.settings.json.example and configure your settings."; \
		exit 1; \
	fi
	@echo "Using apps/data-sync/local.settings.json"
	@echo "Starting function app..."
	@echo "Once running, trigger sync at: http://localhost:7071/api/sync"
	@echo ""
	@cd apps/data-sync && PATH="$(VENV_PATH):$$PATH" func start

# Run data-sync function locally
run-data-sync: _check-azurite
	@echo "Starting data-sync function..."
	@cd apps/data-sync && \
		if [ ! -f local.settings.json ]; then cp local.settings.json.example local.settings.json; fi && \
		PATH="$(VENV_PATH):$$PATH" func start

# Run email-update function locally
run-email-update: _check-azurite _setup-email-update-settings
	@echo "Starting email-update function..."
	@cd apps/email-update && \
		PATH="$(VENV_PATH):$$PATH" func start

_check-azurite:
	@pgrep -f azurite > /dev/null || (echo "Error: Azurite not running. Run 'make azurite-start' first." && exit 1)

_setup-email-update-settings:
	@if [ ! -f apps/email-update/local.settings.json ]; then \
		echo '{\n  "IsEncrypted": false,\n  "Values": {\n    "AzureWebJobsStorage": "$(AZURITE_CONN)",\n    "FUNCTIONS_WORKER_RUNTIME": "python",\n    "BLOB_CONNECTION_STRING": "$(AZURITE_CONN)",\n    "AZURE_STORAGE_CONNECTION_STRING": "$(AZURITE_CONN)",\n    "BLOB_ACCOUNT_URL": "",\n    "BLOB_CONTAINER_NAME": "fec-filings",\n    "MANIFEST_CONTAINER_NAME": "manifests",\n    "EMAIL_CONNECTION_STRING": "",\n    "EMAIL_SENDER_ADDRESS": "test@example.com",\n    "EMAIL_RECIPIENT_LIST": "",\n    "AZURE_OPENAI_ENDPOINT": "",\n    "AZURE_OPENAI_API_KEY": "",\n    "AZURE_OPENAI_DEPLOYMENT": ""\n  }\n}' > apps/email-update/local.settings.json; \
		echo "Created apps/email-update/local.settings.json"; \
	fi

# Build all function packages for deployment
build-functions: build-data-sync build-email-update
	@echo "All function packages built successfully"

# Build data-sync function package
build-data-sync:
	@echo "Building data-sync function package..."
	@rm -rf dist/
	@uv build --wheel packages/fec-api-client --out-dir dist/
	@uv build --wheel packages/services --out-dir dist/
	@uv export --no-hashes --no-emit-package fec-api-client --no-emit-package services -o apps/data-sync/requirements.txt
	@rm -rf apps/data-sync/.python_packages
	@mkdir -p apps/data-sync/.python_packages/lib/site-packages
	@uv pip install --target apps/data-sync/.python_packages/lib/site-packages -r apps/data-sync/requirements.txt dist/*.whl
	@echo "data-sync package built in apps/data-sync/.python_packages"

# Build email-update function package
build-email-update:
	@echo "Building email-update function package..."
	@rm -rf dist/
	@uv build --wheel packages/fec-api-client --out-dir dist/
	@uv build --wheel packages/services --out-dir dist/
	@uv export --no-hashes --no-emit-package fec-api-client --no-emit-package services -o apps/email-update/requirements.txt
	@rm -rf apps/email-update/.python_packages
	@mkdir -p apps/email-update/.python_packages/lib/site-packages
	@uv pip install --target apps/email-update/.python_packages/lib/site-packages -r apps/email-update/requirements.txt dist/*.whl
	@echo "email-update package built in apps/email-update/.python_packages"

# Register all Azure resource providers required by the infrastructure
az-register-providers:
	@echo "Registering Azure resource providers..."
	az provider register --namespace Microsoft.Storage --wait
	az provider register --namespace Microsoft.Web --wait
	az provider register --namespace Microsoft.Insights --wait
	az provider register --namespace Microsoft.OperationalInsights --wait
	az provider register --namespace Microsoft.Communication --wait
	az provider register --namespace Microsoft.CognitiveServices --wait
	az provider register --namespace Microsoft.Authorization --wait
	az provider register --namespace Microsoft.AlertsManagement --wait
	@echo "All providers registered successfully"

clean:
	rm -rf apps/*/local.settings.json
	rm -rf apps/*/.python_packages
	rm -rf apps/*/requirements.txt
	rm -rf apps/*/__pycache__
	rm -rf packages/*/__pycache__
	rm -rf .pytest_cache
	rm -rf dist
	@echo "Cleaned up generated files"

# ============================================================================
# Deployment Targets
# ============================================================================

# Login to Azure CLI
az-login:
	@echo "Logging in to Azure..."
	az login

# Create Azure resource group
az-create-rg:
	@echo "Creating resource group $(AZURE_RESOURCE_GROUP) in $(AZURE_LOCATION)..."
	az group create --name $(AZURE_RESOURCE_GROUP) --location $(AZURE_LOCATION)

# Deploy Azure infrastructure using Bicep
deploy-infra:
ifndef FEC_API_KEY
	$(error FEC_API_KEY is required. Set it with: export FEC_API_KEY=your-key)
endif
	@echo "Deploying infrastructure to $(AZURE_RESOURCE_GROUP)..."
	az deployment group create \
		--resource-group $(AZURE_RESOURCE_GROUP) \
		--template-file infra/main.bicep \
		--parameters environment=$(ENVIRONMENT) \
		--parameters baseName=$(BASE_NAME) \
		--parameters fecApiKey=$(FEC_API_KEY)
	@echo "Infrastructure deployed successfully!"

# Deploy data-sync function app code
deploy-data-sync: build-data-sync
	@echo "Deploying data-sync function to Azure..."
	$(eval DATA_SYNC_APP := $(shell az deployment group show --resource-group $(AZURE_RESOURCE_GROUP) --name main --query 'properties.outputs.functionAppName.value' -o tsv 2>/dev/null || echo ""))
	@if [ -z "$(DATA_SYNC_APP)" ]; then \
		echo "Error: Could not find function app name. Run 'make deploy-infra' first."; \
		exit 1; \
	fi
	cd apps/data-sync && func azure functionapp publish $(DATA_SYNC_APP)
	@echo "data-sync deployed successfully!"

# Deploy email-update function app code
deploy-email-update: build-email-update
	@echo "Deploying email-update function to Azure..."
	$(eval EMAIL_APP := $(shell az deployment group show --resource-group $(AZURE_RESOURCE_GROUP) --name main --query 'properties.outputs.emailFunctionAppName.value' -o tsv 2>/dev/null || echo ""))
	@if [ -z "$(EMAIL_APP)" ]; then \
		echo "Error: Could not find email function app name. Run 'make deploy-infra' first."; \
		exit 1; \
	fi
	cd apps/email-update && func azure functionapp publish $(EMAIL_APP)
	@echo "email-update deployed successfully!"

# Deploy everything: infrastructure + all function apps
deploy-all: deploy-infra deploy-data-sync deploy-email-update
	@echo ""
	@echo "============================================"
	@echo "  Deployment complete!"
	@echo "============================================"
	@echo "  Resource Group: $(AZURE_RESOURCE_GROUP)"
	@echo "  Environment:    $(ENVIRONMENT)"
	@echo "============================================"
