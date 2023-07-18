from strategies.preprocess.simple_binarize import SimpleBinarize


class PreprocessingStrategyFactory:
    def __init__(self):
        self.strategies = {
            'simplebinarize': SimpleBinarize,
            # 'deskew': Deskew,
            # Add more as needed
        }

    def create(self, strategy_name, strategy_type):
        strategy_class = self.strategies.get(strategy_name)
        if not strategy_class:
            raise ValueError(f"Invalid strategy name: {strategy_name}")

        strategy = strategy_class()
        if strategy.strategy_type != strategy_type:
            raise ValueError(f"Strategy type mismatch: strategy {strategy_name} is not of type {strategy_type}")

        return strategy


class PostprocessingStrategyFactory:
    def __init__(self):
        self.strategies = {
            'simplepostprocessing': SimplePostprocessing,
            # Add more as needed
        }

    def create(self, strategy_name, strategy_type):
        strategy_class = self.strategies.get(strategy_name)
        if not strategy_class:
            raise ValueError(f"Invalid strategy name: {strategy_name}")

        strategy = strategy_class()
        if strategy.strategy_type != strategy_type:
            raise ValueError(f"Strategy type mismatch: strategy {strategy_name} is not of type {strategy_type}")

        return strategy