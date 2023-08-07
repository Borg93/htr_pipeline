from htr.enums import StrategyName, StrategyType
from htr.strategies.strategy import Strategy


class SimplePost(Strategy):
    def __init__(self):
        pass

    @property
    def strategy_name(self):
        return StrategyName.SIMPLE_POSTPROCESSING.value

    @property
    def strategy_type(self):
        return StrategyType.POSTPROCESSING.value


    def process(self, input_image):
        # Actual implementation of binarization goes here
        # This is a placeholder, replace it with your actual code
        binarized_image = input_image  # Placeholder
        return binarized_image
