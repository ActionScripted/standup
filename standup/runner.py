import logging

from .config import config
from .registry import registry

logger = logging.getLogger(__name__)


class Runner:
    def __init__(self):
        self.config = config
        self.registry = registry

    def run(self):
        for name, instance in self.registry.providers.items():
            try:
                instance.display()
            except Exception as e:
                logger.error(
                    f"Failed to execute display method for provider {name}: {e}"
                )


if __name__ == "__main__":
    runner = Runner()
    runner.run()
