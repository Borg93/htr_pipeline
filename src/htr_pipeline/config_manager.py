import json


class ConfigManager:
    def __init__(self, config_file_path):
        with open(config_file_path) as config_file:
            self.config_data = json.load(config_file)

    def get_model_name(self):
        return self.config_data.get('model_name')

    def get_model_type(self):
        return self.config_data.get('model_type')

    def get_preprocessing_strategy(self):
        return self.config_data.get('preprocessing_strategy')

    def get_postprocessing_strategy(self):
        return self.config_data.get('postprocessing_strategy')
