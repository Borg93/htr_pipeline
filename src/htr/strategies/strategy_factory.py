from htr.enums import StrategyName
from htr.strategies.base_strategy import Strategy
from htr.strategies.postprocess.simple_postprocessing import SimplePost
from htr.strategies.preprocess.simple_binarize import SimpleBinarize


class StrategyFactory:
    def __init__(self):
        self.strategies = {}

    def register_custom_strategy(self, strategy_name, strategy_type, strategy_class):
        # Ensure the strategy_class is a subclass of Strategy
        if not issubclass(strategy_class, Strategy):
            raise TypeError("strategy_class must be a subclass of Strategy.")
        self.strategies[strategy_name] = strategy_class

    def create(self, strategy_name, strategy_type):
        strategy_class = self.strategies.get(strategy_name)

        if not strategy_class:
            available_strategies = ", ".join(self.strategies.keys())
            raise ValueError(f"Invalid strategy name: {strategy_name}. Available strategies: {available_strategies}")

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
            StrategyName.SIMPLE_POSTPROCESSING.value: SimplePost,
            # Add more as needed
        }