from strategies.strategy import Strategy


class SimpleBinarize(Strategy):
    def __init__(self):
        self._strategy_type = "preprocessing"
        self._strategy_name = "simplebinarize"


    @property
    def strategy_name(self):
        return self._strategy_name

    @property
    def strategy_type(self):
        return self._strategy_type

    def process(self, input_image):
        # Actual implementation of binarization goes here
        # This is a placeholder, replace it with your actual code
        binarized_image = input_image  # Placeholder
        return binarized_image
