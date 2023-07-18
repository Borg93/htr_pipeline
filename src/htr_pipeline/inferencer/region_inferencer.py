from htr_pipeline.inferencer.inferencer import Inferencer
from htr_pipeline.inferencer.visualizers.region_visualizer import RegionVisualizer


class RegionInferencer(Inferencer):
    def __init__(self, model, preprocess_strategies=None, postprocess_strategies=None):
        self.predicted = False
        self._inferencer_type = "region"
        self.model = model
        self.preprocess_strategies = preprocess_strategies or []
        self.postprocess_strategies = postprocess_strategies or []

        if not self.preprocess_strategies:
            print("Warning: No preprocess strategies provided.")
        if not self.postprocess_strategies:
            print("Warning: No postprocess strategies provided.")

    @property
    def inferencer_type(self):
        return self._inferencer_type

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
        raw_output = self.model.predict(preprocessed_image)  # Placeholder
        self.predicted = True  # Indicate that a prediction has been made
        return raw_output

    def visualize(self, raw_output):
        if not self.predicted:
            raise ValueError("Predict method must be run before visualize")
        # Implement the visualization logic specific to the region model here
        visualizer = RegionVisualizer()  # Create a new visualizer here
        visualizer.visualize(raw_output)


