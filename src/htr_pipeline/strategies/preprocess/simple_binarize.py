from strategies.strategy import Strategy


class SimpleBinarize(Strategy):
    def __init__(self):
        super().__init__("region")

    def process(self, input_image):
        # Actual implementation of binarization goes here
        # This is a placeholder, replace it with your actual code
        binarized_image = input_image  # Placeholder
        return binarized_image
