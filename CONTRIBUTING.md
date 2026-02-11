# Contributing to FEC Data Sync & Email Update

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Getting Started

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager
- [Azure Functions Core Tools](https://learn.microsoft.com/azure/azure-functions/functions-run-local)
- [Azurite](https://learn.microsoft.com/azure/storage/common/storage-use-azurite) (local storage emulator)

### Setting Up Your Development Environment

1. Fork the repository and clone your fork
2. Install dependencies:
   ```bash
   make install
   ```
3. Start the local storage emulator:
   ```bash
   make azurite-start
   ```
4. Run the tests to verify your setup:
   ```bash
   make test
   ```

## Development Workflow

### Branch Naming

Use descriptive branch names:
- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates

### Code Style

This project uses:
- **Ruff** for linting and formatting
- **Pyright** for type checking

Run all checks before submitting:
```bash
make lint
```

### Testing

Write tests for new functionality. Run tests with:
```bash
make test
```

For specific test files:
```bash
uv run pytest packages/services/tests/test_your_module.py -v
```

### Commit Messages

Write clear, concise commit messages:
- Use the imperative mood ("Add feature" not "Added feature")
- Keep the first line under 72 characters
- Reference issues when applicable (e.g., "Fix #123")

## Submitting Changes

1. Create a branch from `main`
2. Make your changes with tests
3. Run linting and tests locally
4. Push your branch and create a Pull Request
5. Fill out the PR template with:
   - Summary of changes
   - Testing performed
   - Any breaking changes

### Pull Request Guidelines

- Keep PRs focused on a single change
- Update documentation if adding new features
- Ensure all CI checks pass
- Request review from maintainers

## Project Structure

```
├── apps/
│   ├── data-sync/           # Azure Function: Syncs FEC data
│   └── email-update/        # Azure Function: Email notifications
├── packages/
│   ├── fec-api-client/      # Generated FEC API client
│   └── services/            # Shared services library
├── infra/                   # Azure Bicep templates
└── docs/                    # Documentation
```

### Adding New Features

1. **Services** go in `packages/services/src/services/`
2. **API client changes** regenerate with `make generate-client`
3. **Azure Functions** follow the existing pattern in `apps/`

## Reporting Issues

Use GitHub Issues to report bugs or request features:

- **Bug reports**: Include steps to reproduce, expected vs actual behavior
- **Feature requests**: Describe the use case and proposed solution

For security vulnerabilities, please see [SECURITY.md](./SECURITY.md).

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](./LICENSE).
