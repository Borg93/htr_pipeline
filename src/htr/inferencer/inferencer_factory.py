from htr.enums import StrategyType
from htr.inferencer.inferencers.region_inferencer import RegionInferencer
from htr.inferencer.models.model_factory import ModelFactory
from htr.inferencer.strategies.strategy_factory import (
    PostprocessingStrategyFactory,
    PreprocessingStrategyFactory,
)


class InferencerFactory:
    def __init__(self):
        self.model_factory = ModelFactory()
        self.preprocessing_strategy_factory = PreprocessingStrategyFactory()
        self.postprocessing_strategy_factory = PostprocessingStrategyFactory()
        self.inferencers = {
            'region': RegionInferencer,
            # ... other inferencers
        }

    def create_inferencer(self, config_data):
        # Create model
        model = self.model_factory.create(config_data)

        # Create strategies
        preprocessing_strategies = self._create_strategies(StrategyType.PREPROCESSING, config_data)
        postprocessing_strategies = self._create_strategies(StrategyType.POSTPROCESSING, config_data)

        # Create and return inferencer
        return self._create_specific_inferencer(model, preprocessing_strategies, postprocessing_strategies)

    def _create_strategies(self, strategy_type, config_data):
        strategy_factory = None

        if strategy_type == StrategyType.PREPROCESSING:
            strategy_factory = self.preprocessing_strategy_factory
        elif strategy_type == StrategyType.POSTPROCESSING:
            strategy_factory = self.postprocessing_strategy_factory
        else:
            raise ValueError(f"Invalid strategy type: {strategy_type}")

        strategy_config = config_data.get(strategy_type.value, [])
        return [strategy_factory.create(strategy) for strategy in strategy_config]

    def _create_specific_inferencer(self, model, preprocessing_strategies, postprocessing_strategies):
        model_type = model.model_type

        if model_type not in self.inferencers:
            raise ValueError(f"Unknown model type: {model_type}")

        return self.inferencers[model_type](model, preprocessing_strategies, postprocessing_strategies)

    # Dynamic Registration
    def register_custom_strategy(self, strategy_type, strategy_name, strategy_class):
        if strategy_type == StrategyType.PREPROCESSING:
            self.preprocessing_strategy_factory.register_custom_strategy(strategy_name, strategy_class)
        elif strategy_type == StrategyType.POSTPROCESSING:
            self.postprocessing_strategy_factory.register_custom_strategy(strategy_name, strategy_class)
        else:
            raise ValueError("Invalid strategy type")

    def register_custom_model(self, model_name, model_type, model_class):
        self.model_factory.register_custom_model(model_name, model_type, model_class)
