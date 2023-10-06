# Standup

Automated standups to show what you've done and what you're doing next.

## Quick Start

```bash
git clone git@repo
cd standup

cp standup.example.toml standup.toml

python run_standup.py
```

For more, check out the help via:

```bash
python run_standup.py --help
```

Heads up! Default providers will only read secrets from the environment. This is to avoid keys in a config file in a repo buried in your dotfiles that could be easily forgotten, leaked or deprecated. We recommend setting these in your environment:

```bash
# If your setup is version-controlled, add this to .gitignore:
**/*.secrets.sh

# Add to or create secrets file (e.g. personal.secrets.sh)
export ASANA_TOKEN="ABCDEFGHIJKLMNOP123456"
export GITHUB_TOKEN="ghp_abcdefghijlkmnop1234567890"
export JIRA_TOKEN="ABCDEFGHIJKLMNOP123456"

# Source secrets in your shell config:
source "$XDG_CONFIG_HOME"/shell/hosts/personal.secrets.sh
```

Make sure `standup.toml` keys match the names set in the environment and you should be all set!

## Adding Providers

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
