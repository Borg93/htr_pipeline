import json
import logging


class ConfigManager:
    def __init__(self):
        self.config_data = {}

    def read(self, config_file_path):
        try:
            with open(config_file_path) as config_file:
                self.config_data = json.load(config_file)
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
