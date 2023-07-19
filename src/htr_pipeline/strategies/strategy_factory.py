from strategies.preprocess.simple_binarize import SimpleBinarize

from htr_pipeline.enums import StrategyName


class StrategyFactory:
    def __init__(self):
        self.strategies = {}

    def create(self, strategy_name, strategy_type):
        strategy_class = self.strategies.get(strategy_name)
        if not strategy_class:
            raise ValueError(f"Invalid strategy name: {strategy_name}")

        strategy = strategy_class()
        if strategy.strategy_type != strategy_type:
            raise ValueError(f"Strategy type mismatch: strategy {strategy_name} is not of type {strategy_type}")

        return strategy


class PreprocessingStrategyFactory(StrategyFactory):
    def __init__(self):
        super().__init__()
        self.strategies = {
            StrategyName.SIMPLE_BINARIZE.value: SimpleBinarize,
            # 'deskew': Deskew,
            # Add more as needed
        }


class PostprocessingStrategyFactory(StrategyFactory):
    def __init__(self):
        super().__init__()
        self.strategies = {
            StrategyName.SIMPLE_POSTPROCESSING.value: SimplePostprocessing,
            # Add more as needed
        }
