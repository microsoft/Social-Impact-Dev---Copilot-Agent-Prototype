.PHONY: help install lint test build azurite-start azurite-stop run-data-sync run-email-update clean az-register-providers

VENV_PATH := $(shell pwd)/.venv/bin
AZURITE_CONN := DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Development:"
	@echo "  install          Install all dependencies"
	@echo "  lint             Run linting and type checks"
	@echo "  test             Run tests"
	@echo ""
	@echo "Local Testing:"
	@echo "  azurite-start    Start Azurite (Azure Storage emulator)"
	@echo "  azurite-stop     Stop Azurite"
	@echo "  run-data-sync    Run data-sync function locally"
	@echo "  run-email-update Run email-update function locally"
	@echo ""
	@echo "Azure:"
	@echo "  az-register-providers  Register required Azure resource providers"
	@echo ""
	@echo "Cleanup:"
	@echo "  clean            Remove generated files"

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
