# Standup

Automated standups using provider APIs to discover what you've done and what you're doing next.

## Quick Start

```bash
git clone git@repo
cd standup

cp standup.example.toml standup.toml

python run_standup.py
```

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
