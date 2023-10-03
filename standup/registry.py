import inspect
import logging
from importlib import import_module

from standup.providers import BaseProvider

logger = logging.getLogger(__name__)


DEFAULT_PROVIDERS = [
    "standup.providers.github",
    "standup.providers.jira",
]


class Registry:
    def __init__(self, providers=None):
        if providers is None:
            providers = []

        for provider in providers:
            self.load(provider)

    def __repr__(self):
        return f"<Providers {self.__dict__}>"

    def load(self, provider):
        try:
            module = import_module(provider)
            for name, candidate in inspect.getmembers(module, inspect.isclass):
                if (
                    issubclass(candidate, BaseProvider)
                    and candidate is not BaseProvider
                ):
                    self.__dict__[candidate.name] = candidate()
        except ImportError:
            logger.error(f"Unable to load provider: {provider}")


providers = Registry(providers=DEFAULT_PROVIDERS)
