from . import BaseProvider


class JiraProvider(BaseProvider):
    """Jira provider."""

    name = "jira"

    def display(self):
        """Display provider data."""
        print("Jira!")
