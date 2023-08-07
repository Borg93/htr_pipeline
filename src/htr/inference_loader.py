import logging

from htr_pipeline.enums import ConfigKey, StrategyType
from htr_pipeline.inferencer.inferencer_factory import InferencerFactory
from htr_pipeline.models.model_factory import ModelFactory
from htr_pipeline.strategies.strategy_factory import PostprocessingStrategyFactory, PreprocessingStrategyFactory


class InferencerLoader:
    def __init__(self, config_manager, inferencers):
        self.config_manager = config_manager
        self.inferencers = inferencers
        self.model_factory = ModelFactory()
        self.inferencer_factory = InferencerFactory()
        self.preprocessing_strategy_factory = PreprocessingStrategyFactory()
        self.postprocessing_strategy_factory = PostprocessingStrategyFactory()

    def _get_inferencer_key(self, model_name, model_type):
        return f"{model_name}_{model_type}"

    def _is_already_loaded(self, inferencer_key, model_name):
        if inferencer_key in self.inferencers:
            logging.info(f"Configuration for model {model_name} already loaded, reusing existing inferencer.")
            return True
        logging.info(f"Loading {inferencer_key}.")
        return False

    def _load_and_register(self, inferencer_key, model_name, model_type, config_data):
        try:
            model = self.model_factory.create(model_name, model_type, config_data)
            print(model)

            preprocessing_strategies = self._create_strategies(StrategyType.PREPROCESSING)
            postprocessing_strategies = self._create_strategies(StrategyType.POSTPROCESSING)
            print(preprocessing_strategies)

            inferencer = self.inferencer_factory.create(model, preprocessing_strategies, postprocessing_strategies)

            print(inferencer)

            self.inferencers[inferencer_key] = inferencer
        except Exception as e:
            logging.error(f"Failed to load model: {str(e)}")

    def _create_strategies(self, strategy_type: StrategyType):
        strategy_factory = self._get_strategy_factory(strategy_type)

        print("strategy_factory: ", strategy_factory)
        
        strategy_config = self.config_manager.get(strategy_type.value)
        if not strategy_config:
            logging.info(f"INFO: No configuration found for strategy type: {strategy_type}.")
            return []

        return [strategy_factory.create(strategy, strategy_type.value) for strategy in strategy_config]

    def _get_strategy_factory(self, strategy_type):
        if strategy_type == StrategyType.PREPROCESSING:
            return self.preprocessing_strategy_factory
        elif strategy_type == StrategyType.POSTPROCESSING:
            return self.postprocessing_strategy_factory
        else:
            raise ValueError("Invalid strategy type")

    def load(self, config_data):
        self.config_manager.add_config(config_data)
        model_name = self.config_manager.get(ConfigKey.MODEL_NAME.value)
        model_type = self.config_manager.get(ConfigKey.MODEL_TYPE.value)

        inferencer_key = self._get_inferencer_key(model_name, model_type)

        if self._is_already_loaded(inferencer_key, model_name):
            return

        self._load_and_register(inferencer_key, model_name, model_type, config_data)


# TODO make it possible for the user to add strat and model dynamically. As long they based
# on the baseclass it is okej.
    def register_custom_strategy(self, strategy_type, strategy_name, strategy_class):
        strategy_factory = self._get_strategy_factory(strategy_type)
        strategy_factory.register_custom_strategy(strategy_name, strategy_class)

    def register_custom_model(self, model_name, model_type, model_class):
        self.model_factory.register_custom_model(model_name, model_type, model_class)

