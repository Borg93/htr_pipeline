from htr.inferencer.base_inferencer import Region
from htr.inferencer.visualizers.region_visualizer import RegionVisualizer


class RegionInferencer(Region):
    def __init__(self, model, preprocess_strategies=None, postprocess_strategies=None):
        super().__init__(model, preprocess_strategies, postprocess_strategies)

    def preprocess(self, input_image):
        for strategy in self.preprocess_strategies:
            input_image = strategy.process(input_image)
        return input_image

    def postprocess(self, output):
        for strategy in self.postprocess_strategies:
            output = strategy.process(output)
        return output

    def predict(self, preprocessed_image):
        # Implement the prediction logic specific to the region model here
        standard_format = self.model.predict(preprocessed_image)  # Placeholder
        self.predicted = True  # Indicate that a prediction has been made
        return standard_format

    def visualize(self, raw_output):
        if not self.predicted:
            raise ValueError("Predict method must be run before visualize")
        # Implement the visualization logic specific to the region model here
        visualizer = RegionVisualizer()  # Create a new visualizer here
        visualizer.visualize(raw_output)
