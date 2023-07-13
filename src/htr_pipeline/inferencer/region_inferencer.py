from htr_pipeline.inferencer.inferencer import Inferencer


class RegionInferencer(Inferencer):
    def __init__(self, model, visualizer):
        super().__init__(model, visualizer)

    def preprocess(self, input_image):
        # Implement your preprocessing logic here
        preprocessed_image = input_image  # Placeholder
        return preprocessed_image

    def predict(self, preprocessed_image):
        # Implement the prediction logic specific to the region model here
        raw_output = self.model.predict(preprocessed_image)  # Placeholder
        self.predicted = True  # Indicate that a prediction has been made
        return raw_output

    def postprocess(self, raw_output):
        # Implement your postprocessing logic here
        processed_output = raw_output  # Placeholder
        return processed_output

    def visualize(self, raw_output):
        if not self.predicted:
            raise ValueError("Predict method must be run before visualize")
        # Implement the visualization logic specific to the region model here
        self.visualizer.visualize(raw_output)
