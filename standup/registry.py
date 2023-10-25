import inspect
import logging
from importlib import import_module
from typing import List, Optional

from standup.config import config
from standup.providers import BaseProvider

logger = logging.getLogger(__name__)


class Registry:
    """Registry to load and manage providers.

    Attributes:
        _instance: Holds the single instance of the Registry class.
        providers: A dictionary containing loaded provider instances keyed by their name.
    """

    _instance: Optional["Registry"] = None
    providers: dict = {}

    def __new__(cls, config: Optional[dict] = None) -> "Registry":
        """Ensure only one instance of the Registry class is instantiated."""
        if config and not cls._instance:
            cls._instance = super(Registry, cls).__new__(cls)
            cls._instance.providers = {}

            if config.items():
                for module_name, module_config in config.items():
                    if module_config["enabled"]:
                        cls._instance.load(module_name, module_config)

        return cls._instance

    def __repr__(self) -> str:
        """Return a readable representation of the Registry object."""
        return f"<Providers {list(self.providers.keys())}>"

    def load(self, provider_module: str, provider_config: dict) -> None:
        """Load the specified provider module and instantiate its classes.

        Args:
            provider: The name of the provider module to load.
        """
        try:
            module = import_module(provider_module)
            for _, candidate in inspect.getmembers(module, inspect.isclass):
                if (
                    issubclass(candidate, BaseProvider)
                    and candidate is not BaseProvider
                ):
                    self.providers[candidate.name] = candidate(provider_config)
        except ImportError:
            logger.error(f"Unable to load provider: {provider_module}")


# TODO: config.config.config.config...config?
registry: Registry = Registry(config=config.config)
