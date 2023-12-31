.DEFAULT_GOAL := help

.PHONY: all backup clean help test setup

backup: ## Backup config files
	@echo "Backing up existing config..."
	@find . -name "standup.toml" -exec mkdir -p backups \; -exec mv {} backups/standup.$(shell date +%s).toml \;

help: ## Show help
	@echo "Usage: make [recipe]\n\nRecipes:"
	@grep -h '##' $(MAKEFILE_LIST) | grep -v grep | sed -e 's/\(.*\):.*## \(.*\)/\1|    \2/' | tr '|' '\n'

run: ## Run standup
	@. .venv/bin/activate && python run_standup.py

setup: backup ## Setup config, environment, etc.
	@cp standup.example.toml standup.toml
	@echo "Creating virtual environment..."
	@python3 -m venv .venv
