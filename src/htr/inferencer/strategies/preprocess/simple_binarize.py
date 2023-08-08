from htr.enums import StrategyName, StrategyType
from htr.inferencer.strategies.base_strategy import Strategy


class SimpleBinarize(Strategy):
    def __init__(self):
        self._strategy_type = StrategyType.PREPROCESSING.value
        self._strategy_name = StrategyName.SIMPLE_BINARIZE.value

    @property
    def strategy_type(self):
        return self._strategy_type

    @property
    def strategy_name(self):
        return self._strategy_name

    def process(self, input_image):
        # Actual implementation of binarization goes here
        # This is a placeholder, replace it with your actual code
        binarized_image = input_image  # Placeholder
        return binarized_image
