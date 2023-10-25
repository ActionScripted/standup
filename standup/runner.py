import logging

logger = logging.getLogger(__name__)


class Runner:
    """Executing the display method of each registered provider.

    Attributes:
        config: A reference to the application's configuration instance.
        registry: A reference to the application's provider registry instance.
    """

    def __init__(self) -> None:
        """Initialize Runner with configuration and registry instances."""
        # self.config = config
        # self.registry = registry

    def run(self) -> None:
        """Execute the display method for each provider in the registry.

        For each provider, the method will attempt to execute its display function.

        If an exception is encountered, it logs the error without stopping the
        execution of other providers.
        """

        # TODO: Consider ditching singletons so we don't do anything on import.
        from .registry import registry

        for name, instance in registry.providers.items():
            try:
                instance.display()
            except Exception as e:
                logger.error(
                    f"Failed to execute display method for provider {name}: {e}"
                )
