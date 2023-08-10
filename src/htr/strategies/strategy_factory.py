from htr.strategies.base_strategy import Strategy
from htr.strategies.postprocess.simple_postprocessing import SimplePost
from htr.strategies.preprocess.simple_binarize import SimpleBinarize


class StrategyFactory:
    def __init__(self):
        self.preprocessing = "preprocessing"
        self.postprocessing = "postprocessing"
        self.strategies = {
            SimpleBinarize.__name__: SimpleBinarize,
            SimplePost.__name__: SimplePost,
            # Add more as needed
        }

    def register_custom_strategy(self, strategy_name, strategy_class):
        if not issubclass(strategy_class, Strategy):
            raise TypeError("strategy_class must be a subclass of Strategkky.")
        self.strategies[strategy_name] = strategy_class

    def create(self, strategy_name, strategy_type):
        strategy_class = self.strategies.get(strategy_name)

        if not strategy_class:
            available_strategies = ", ".join(self.strategies.keys())
            raise ValueError(f"Invalid strategy name: {strategy_name}. Available strategies: {available_strategies}")

        if strategy_class.strategy_type != strategy_type:
            raise ValueError(f"Strategy type mismatch: strategy {strategy_name} is not of type {strategy_type}")

        strategy = strategy_class()

        return strategy
