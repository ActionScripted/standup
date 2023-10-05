from . import BaseProvider


class AsanaProvider(BaseProvider):
    """Asana provider."""

    name = "asana"

    def display(self):
        """Display provider data."""
        print("Asana!")
