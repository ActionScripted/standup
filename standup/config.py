import pathlib
import tomllib

CONFIG_FILE = "standup.toml"


class Config:
    def __init__(self, file_name=CONFIG_FILE):
        file = pathlib.Path(file_name)

        if not file.exists():
            raise FileNotFoundError(f"Unable to find config file: {file_name}")

        self._config = tomllib.loads(file.read_text())

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return self._config[name]

    def __repr__(self):
        return f"<Config {self._config}>"


config = Config()
