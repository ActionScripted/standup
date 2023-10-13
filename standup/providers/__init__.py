import os
from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """Base class for providers."""

    def __init__(self, config: dict):
        """Initialize the provider."""
        self.config = config
        self.load_env()

    def load_env(self):
        """Load environment variables."""
        for key, value in self.config.items():
            if key.startswith("env_"):
                env_value = os.getenv(value, None)

                if env_value is None:
                    raise ValueError(
                        f"{value} is not set! Please set environment variable or disable {self.name} provider."
                    )

                setattr(self, key, env_value)

    @abstractmethod
    def display(self):
        """Display provider data.

        This can be whatever might be appropriate for the provider.

        For example if the provider is a to do list, you might show
        items that were completed N days ago. If you do date stuff
        don't forget to account for weekends!
        """
        raise NotImplementedError
