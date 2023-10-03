import inspect
import logging
from importlib import import_module
from typing import List, Optional

from standup.config import config
from standup.providers import BaseProvider

logger = logging.getLogger(__name__)


class Registry:
    """A singleton registry class to load and manage providers.

    Attributes:
        _instance: Holds the single instance of the Registry class.
        providers: A dictionary containing loaded provider instances keyed by their name.
    """

    _instance: Optional["Registry"] = None

    def __new__(cls, providers: Optional[List[str]] = None) -> "Registry":
        """Ensure only one instance of the Registry class is instantiated."""
        if not cls._instance:
            cls._instance = super(Registry, cls).__new__(cls)
            cls._instance.providers = {}

            if providers:
                for provider in providers:
                    cls._instance.load(provider)

        return cls._instance

    def __repr__(self) -> str:
        """Return a readable representation of the Registry object."""
        return f"<Providers {list(self.providers.keys())}>"

    def load(self, provider: str) -> None:
        """Load the specified provider module and instantiate its classes.

        Args:
            provider: The name of the provider module to load.
        """
        try:
            module = import_module(provider)
            for name, candidate in inspect.getmembers(module, inspect.isclass):
                if (
                    issubclass(candidate, BaseProvider)
                    and candidate is not BaseProvider
                ):
                    self.providers[candidate.name] = candidate()
        except ImportError:
            logger.error(f"Unable to load provider: {provider}")


registry: Registry = Registry(providers=config.providers)
