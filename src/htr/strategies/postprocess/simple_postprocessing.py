from htr.strategies.base_strategy import PostProcessing


class SimplePost(PostProcessing):
    def __init__(self):
        pass

    def process(self, input_image):
        # Actual implementation of binarization goes here
        # This is a placeholder, replace it with your actual code
        binarized_image = input_image  # Placeholder
        return binarized_image
