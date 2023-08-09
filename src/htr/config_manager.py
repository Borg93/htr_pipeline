import json
import os


class ConfigManager:
    def __init__(self):
        self.configs = {}

    def add_config(self, key, config_data_or_path):
        config_data = self._get_config_data(config_data_or_path)
        if key in self.configs:
            raise ValueError(f"Key: {key} is already in use. Please use a different key.")
        self.configs[key] = config_data

    def get_config(self, key):
        return self.configs.get(key)

    def _get_config_data(self, config_data_or_path):
        if isinstance(config_data_or_path, dict):
            return config_data_or_path
        elif isinstance(config_data_or_path, str):
            if os.path.isdir(config_data_or_path):
                config_data_or_path = os.path.join(config_data_or_path, 'config.json')
            with open(config_data_or_path, 'r') as file:
                return json.load(file)
        else:
            raise TypeError("config_data_or_path must be a dictionary or a path.")


if __name__ == "__main__":
    config_dict = {
        "model_name": "RmtDetRegion",
        "model_hf": "Riksarkivet/HTR_pipeline_models",
        "model_type": "region",
        "preprocessing": ["simplebinarize", "resize"],
        "postprocessing": "simplepostprocessing",
        "verbose": True
    }
    config_manager = ConfigManager()
    config_manager.add_config("dict_test",config_dict)
    config_manager.add_config("path_test","/home/gabriel/Desktop/htr_pipeline/notebooks/RmtDet")


    print(config_manager.configs)

