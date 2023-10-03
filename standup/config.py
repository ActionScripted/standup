import pathlib
import tomllib

CONFIG_FILE = "standup.toml"


class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._file_path = pathlib.Path(CONFIG_FILE)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        if not self._file_path.exists():
            raise FileNotFoundError(f"Unable to find config file: {self._file_path}")

        self._config = tomllib.loads(self._file_path.read_text())

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return self._config.get(name, None)

    def __repr__(self):
        return f"<Config {self._config}>"


config = Config()
