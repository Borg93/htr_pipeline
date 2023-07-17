class PreprocessingStrategyFactory:
    def __init__(self):
        self.strategies = {
            'simplebinarize': SimpleBinarize,
            'deskew': Deskew,
            # Add more as needed
        }

    def create(self, strategy_type):
        if strategy_type not in self.strategies:
            raise ValueError(f"Unknown preprocessing strategy type: {strategy_type}")

        return self.strategies[strategy_type]()


class PostprocessingStrategyFactory:
    def __init__(self):
        self.strategies = {
            'simplepostprocessing': SimplePostprocessing,
            # Add more as needed
        }

    def create(self, strategy_type):
        if strategy_type not in self.strategies:
            raise ValueError(f"Unknown postprocessing strategy type: {strategy_type}")

        return self.strategies[strategy_type]()
