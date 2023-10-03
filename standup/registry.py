import inspect
import logging
from importlib import import_module

from standup.config import config
from standup.providers import BaseProvider

logger = logging.getLogger(__name__)


class Registry:
    _instance = None

    def __new__(cls, providers=None):
        if not cls._instance:
            cls._instance = super(Registry, cls).__new__(cls)
            cls._instance.providers = {}

            if providers:
                for provider in providers:
                    cls._instance.load(provider)

        return cls._instance

    def __repr__(self):
        return f"<Providers {list(self.providers.keys())}>"

    def load(self, provider):
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


registry = Registry(providers=config.providers)
