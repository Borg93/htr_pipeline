from htr.config_manager import ConfigManager
from htr.inferencer.inferencer_factory import InferencerFactory
from htr.models.model_factory import ModelFactory
from htr.strategies.strategy_factory import StrategyFactory


class InferencerLoader:
    def __init__(
        self,
        inferencer_factory=InferencerFactory(),
        model_factory=ModelFactory(),
        strategy_factory=StrategyFactory(),
        config_manager=ConfigManager(),
    ):
        self.model_factory = model_factory
        self.strategy_factory = strategy_factory
        self.inferencer_factory = inferencer_factory
        self.config_manager = config_manager
        self.inferencers = {}

    def get_inferencer_details(self, inferencer_key):
        inferencer = self.inferencers.get(inferencer_key)
        if not inferencer:
            raise ValueError(f"Inferencer with key {inferencer_key} not found.")
        return inferencer.details

    def load_inferencer(self, key, config_data_or_path):
        # Add the configuration to the ConfigManager
        self.config_manager.add_config(key, config_data_or_path)

        # Fetch the configuration data
        config_data = self.config_manager.get_config(key)

        # Create model
        model = self.model_factory.create(
            config_data[self.model_factory.model_name], config_data[self.model_factory.model_type], config_data
        )

        # Create strategies
        preprocessing_strategies = self._create_strategies(self.strategy_factory.preprocessing, config_data)
        postprocessing_strategies = self._create_strategies(self.strategy_factory.postprocessing, config_data)

        # Create and store the inferencer
        inferencer = self.inferencer_factory.create_inferencer(
            model, preprocessing_strategies, postprocessing_strategies
        )
        self.inferencers[key] = inferencer

    def _create_strategies(self, strategy_type, config_data):
        strategy_names = config_data[strategy_type]

        if isinstance(strategy_names, str):
            strategy_names = [strategy_names]

        return [self.strategy_factory.create(name, strategy_type) for name in strategy_names]

    # # Dynamic Registration (delegating to the factory)
    # def register_custom_strategy(self, strategy_name, strategy_type, strategy_class):
    #     if strategy_type == self.preprocessing_str:
    #         self.preprocessing_strategy_factory.register_custom_strategy(strategy_name, strategy_type, strategy_class)
    #     elif strategy_type == self.postprocessing_str:
    #         self.postprocessing_strategy_factory.register_custom_strategy(strategy_name, strategy_type, strategy_class)
    #     else:
    #         raise ValueError("Invalid strategy type")

    # def register_custom_model(self, model_name, model_type, model_class):
    #     self.model_factory.register_custom_model(model_name, model_type, model_class)
