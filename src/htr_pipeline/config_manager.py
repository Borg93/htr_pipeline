import json
import logging
import os


class ConfigManager:
    def __init__(self):
        self.configs = {}  # Store configs by their model_name

    def read(self, folder_path):
        try:
            config_file_path = os.path.join(folder_path, 'config.json')

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

    def get(self, key, model_name=None, default_value=None):
        config_data = self.configs[model_name] if model_name else self.config_data
        return config_data.get(key, default_value)

    def list_keys(self, model_name=None):
        config_data = self.configs[model_name] if model_name else self.config_data
        return list(config_data.keys())
