import json
import logging


class ConfigManager:
    def __init__(self):
        self.configs = {}  # Store configs by their model_name

    def read(self, config_file_path):
        try:
            with open(config_file_path) as config_file:
                new_config = json.load(config_file)
                model_name = new_config.get('model_name')

                if model_name in self.configs:
                    if self.configs[model_name] != new_config:
                        raise ValueError(f"Model name {model_name} is already used with a different configuration.")
                else:
                    self.configs[model_name] = new_config

                self.config_data = new_config
        except FileNotFoundError:
            logging.error(f"Config file not found: {config_file_path}")
            raise
        except json.JSONDecodeError:
            logging.error(f"Failed to parse config file: {config_file_path}")
            raise

    def get(self, key):
        try:
            return self.config_data[key]
        except KeyError:
            logging.error(f"Key not found in config data: {key}")
            raise

