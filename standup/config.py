import pathlib
import tomllib
from typing import Any

from .utils import recursive_update


class Config:
    """Configuration to load and access configurations from TOML file.

    Attributes:
        _file: The path to the TOML configuration file.
        _instance: Holds the single instance of the Config class.
        config: The loaded configuration as a dictionary.
        defaults: The default configuration as a dictionary.
    """

    _file = "standup.toml"
    _instance = None

    config: dict = {}
    defaults = {
        "standup.providers.asana": {
            "enabled": False,
        },
        "standup.providers.github": {
            "enabled": False,
        },
        "standup.providers.jira": {
            "enabled": False,
        },
    }

    def __new__(cls, *args, **kwargs) -> "Config":
        """Ensure only one instance of the Config class is instantiated."""
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_config()

        return cls._instance

    def _load_config(self) -> None:
        """Load the configuration from the TOML file into config attribute."""
        file = pathlib.Path(self._file)

        if not file.exists():
            raise FileNotFoundError(f"Unable to find config file: {file}")

        config = tomllib.loads(file.read_text())

        # Merge defaults with loaded config
        self.config = recursive_update(self.defaults, config)

    def __getattribute__(self, name: str) -> Any:
        """Override to get attributes from config dictionary if they're not present."""
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return self.config.get(name, None)

    def __repr__(self) -> str:
        """Return a readable representation of the Config object."""
        return f"<Config {self.config.keys()}>"


config: Config = Config()
