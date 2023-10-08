# Standup

Automated standups to show what you've done and what you're doing next.

## Quick Start

```bash
# Copy repo locally
git clone git@repo
cd standup

# Initialize config, environment, etc.
make setup

# Run standup!
make run
```

## Secrets

Default providers will only read secrets from the environment. This is to avoid keys in a config file in a repo buried in your dotfiles that could be easily forgotten, leaked or deprecated. We recommend setting these in your environment:

```bash
# If your setup is version-controlled, add this to .gitignore:
**/*.secrets.sh

# Add to or create secrets file (e.g. personal.secrets.sh)
export ASANA_TOKEN="ABCDEFGHIJKLMNOP123456"
export GITHUB_TOKEN="ABCDEFGHIJKLMNOP123456"
export JIRA_TOKEN="ABCDEFGHIJKLMNOP123456"
# ...etc.

# Source secrets in your shell config:
source "$XDG_CONFIG_HOME"/shell/hosts/personal.secrets.sh
```

Make sure `standup.toml` keys match the names set in the environment and you should be all set!

## Creating Providers

Create a local provider by creating `./local/providers/example.py`:

```python
from standup.providers import BaseProvider

class ExampleProvider(BaseProvider):
    """Example provider."""

    name = "example"

    def display(self):
        """Display provider data."""
        print("Local example! Get to work.")
```

Update `standup.toml` to include your provider:

```toml
providers = [
    # ...other providers here, maybe...
    "local.providers.example",
]
```

**We strongly suggest pulling secrets from the environment and not from the configuration file.** You can do whatever you want -- it's your provider! -- but we don't think it's a good idea to keep long-lived keys for the types of services we're reading from buried in a configuration file for a project like this.
