import json
import logging


class ConfigManager:
    def __init__(self, config_dict=None):
        self.configs = {}  # Store configs by their model_name

        if config_dict is not None:
            self.add_config(config_dict)

    def add_config(self, config_dict):
        model_name = config_dict.get('model_name')

        if model_name in self.configs:
            if self.configs[model_name] != config_dict:
                raise ValueError(f"Model name {model_name} is already used with a different configuration.")
        else:
            self.configs[model_name] = config_dict

        self.config_data = config_dict

    def get(self, key, model_name=None, default_value=None):
        config_data = self.configs[model_name] if model_name else self.config_data
        return config_data.get(key, default_value)

    def list_keys(self, model_name=None):
        config_data = self.configs[model_name] if model_name else self.config_data
        return list(config_data.keys())

    def load_from_file(self, filepath):
        with open(filepath, 'r') as file:
            config_dict = json.load(file)
        self.add_config(config_dict)


if __name__ == "__main__":
    config_dict = {
        "model_name": "RmtDetRegion",
        "model_hf": "Riksarkivet/HTR_pipeline_models",
        "model_type": "region",
        "preprocessing": ["simplebinarize", "resize"],
        "postprocessing": "simplepostprocessing",
        "verbose": True
    }
    config_manager = ConfigManager(config_dict)

