import pathlib
import tomllib
from typing import Any

CONFIG_FILE = "standup.toml"


class Config:
    """A singleton configuration class to load and access configurations from a TOML file.

    Attributes:
        _config: The loaded configuration as a dictionary.
        _file_path: The path to the TOML configuration file.
        _instance: Holds the single instance of the Config class.
    """

    _instance = None

    def __new__(cls, *args, **kwargs) -> "Config":
        """Ensure only one instance of the Config class is instantiated."""
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._file_path = pathlib.Path(CONFIG_FILE)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self) -> None:
        """Load the configuration from the TOML file into _config attribute."""
        if not self._file_path.exists():
            raise FileNotFoundError(f"Unable to find config file: {self._file_path}")

        self._config = tomllib.loads(self._file_path.read_text())

    def __getattribute__(self, name: str) -> Any:
        """Override to get attributes from _config dictionary if they're not present."""
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return self._config.get(name, None)

    def __repr__(self) -> str:
        """Return a readable representation of the Config object."""
        return f"<Config {self._config}>"


config: Config = Config()
