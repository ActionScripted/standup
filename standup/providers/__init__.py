from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """Base class for providers."""

    def __init__(self, config: dict):
        """Initialize the provider."""
        self.config = config

    @abstractmethod
    def display(self):
        """Display provider data.

        This can be whatever might be appropriate for the provider.

        For example if the provider is a to do list, you might show
        items that were completed N days ago. If you do date stuff
        don't forget to account for weekends!
        """
        raise NotImplementedError
