from strategies.strategy import Strategy

from htr_pipeline.enums import StrategyName, StrategyType


class SimpleBinarize(Strategy):
    def __init__(self):
        pass

    @property
    def strategy_name(self):
        return StrategyName.SIMPLE_BINARIZE.value

    @property
    def strategy_type(self):
        return StrategyType.PREPROCESSING.value

    def process(self, input_image):
        # Actual implementation of binarization goes here
        # This is a placeholder, replace it with your actual code
        binarized_image = input_image  # Placeholder
        return binarized_image
