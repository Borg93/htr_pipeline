from htr_pipeline.inferencer.inferencer import Inferencer
from htr_pipeline.inferencer.visualizers.region_visualizer import RegionVisualizer


class RegionInferencer(Inferencer):
    def __init__(self, model):
        model_type = model.get_model_type()
        if model_type != 'region':
            raise ValueError(f"The model type for {model.__class__.__name__} should be 'region', got '{model_type}' instead.")
        super().__init__(model)

    def preprocess(self, input_image):
        # Implement your preprocessing logic here
        preprocessed_image = input_image  # Placeholder
        return preprocessed_image

    def predict(self, preprocessed_image):
        # Implement the prediction logic specific to the region model here
        raw_output = self.model.predict(preprocessed_image)  # Placeholder
        self.predicted = True  # Indicate that a prediction has been made
        print(raw_output)
        print("region inferencer predicted.")
        return raw_output

    def postprocess(self, raw_output):
        # Implement your postprocessing logic here
        processed_output = raw_output  # Placeholder
        return processed_output

    def visualize(self, raw_output):
        if not self.predicted:
            raise ValueError("Predict method must be run before visualize")
        # Implement the visualization logic specific to the region model here
        visualizer = RegionVisualizer()  # Create a new visualizer here
        visualizer.visualize(raw_output)

