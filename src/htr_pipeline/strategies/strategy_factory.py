from strategies.preprocess.simple_binarize import SimpleBinarize


class PreprocessingStrategyFactory:
    def __init__(self):
        self.strategies = {
            'simplebinarize': SimpleBinarize,
            # 'deskew': Deskew,
            # Add more as needed
        }

    def create(self, strategy_type, model_type):
        if strategy_type not in self.strategies:
            raise ValueError(f"Unknown preprocessing strategy type: {strategy_type}")
        strategy = self.strategies[strategy_type]()
        if strategy.strategy_type != model_type:
            raise ValueError(f"Strategy {strategy_type} is not valid for model type {model_type}")
        return strategy


class PostprocessingStrategyFactory:
    def __init__(self):
        self.strategies = {
            'simplepostprocessing': SimplePostprocessing,
            # Add more as needed
        }

    def create(self, strategy_type, model_type):
        if strategy_type not in self.strategies:
            raise ValueError(f"Unknown postprocessing strategy type: {strategy_type}")
        strategy = self.strategies[strategy_type]()
        if strategy.strategy_type != model_type:
            raise ValueError(f"Strategy {strategy_type} is not valid for model type {model_type}")
        return strategy
