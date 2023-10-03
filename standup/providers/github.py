from . import BaseProvider


class GitHubProvider(BaseProvider):
    """GitHub provider."""

    name = "github"

    def display(self):
        """Display provider data."""
        print("GitHub!")
