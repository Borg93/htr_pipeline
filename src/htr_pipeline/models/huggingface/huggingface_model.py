from htr_pipeline.models.model import Model


class HuggingFaceModel(Model):
    def __init__(self, model_name):
        pass
        # Load the Hugging Face model here

    def preprocess(self, input):
        pass
        # Implement your preprocessing logic here

    def postprocess(self, raw_output):
        pass
        # Implement your postprocessing logic here


    def predict(self, input):
        pass
        # Implement your prediction logic here


