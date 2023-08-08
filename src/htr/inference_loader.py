import logging

from htr.config_manager import ConfigManager
from htr.enums import ConfigFile, ConfigKey  # TODO implement this
from htr.inferencer.inferencer_factory import InferencerFactory


class InferencerLoader:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.inferencers = {}
        self.inferencer_factory = InferencerFactory()

    def load_inferencer(self, config_data_or_path):
        # Configuration Management
        config_data = self._get_config_data(config_data_or_path)

        inferencer_key = self._generate_inferencer_key(config_data)

        # Caching
        if self._is_already_loaded(inferencer_key):
            return self.inferencers[inferencer_key]

        # Use the factory to create the inferencer
        inferencer = self.inferencer_factory.create_inferencer(config_data)
        self.inferencers[inferencer_key] = inferencer

        # Lifecycle Management: Initialization (if needed)
        if hasattr(inferencer, 'initialize'):
            inferencer.initialize()

        return inferencer

    def _get_config_data(self, config_data_or_path):
        if isinstance(config_data_or_path, dict):
            return config_data_or_path
        elif isinstance(config_data_or_path, str):
            return self.config_manager.load_from_path(config_data_or_path)
        else:
            raise TypeError("config_data_or_path must be a dictionary or a path.")

    def _generate_inferencer_key(self, config_data):
        # Generate a unique key for the inferencer based on the config_data
        return hash(str(config_data))

    def _is_already_loaded(self, inferencer_key):
        return inferencer_key in self.inferencers

    # Dynamic Registration (delegating to the factory)
    def register_custom_strategy(self, strategy_type, strategy_name, strategy_class):
        self.inferencer_factory.register_custom_strategy(strategy_type, strategy_name, strategy_class)

    def register_custom_model(self, model_name, model_type, model_class):
        self.inferencer_factory.register_custom_model(model_name, model_type, model_class)


    # Lifecycle Management: Cleanup (if needed)
    def cleanup(self, inferencer_key):
        inferencer = self.inferencers.get(inferencer_key)
        if inferencer and hasattr(inferencer, 'cleanup'):
            inferencer.cleanup()


