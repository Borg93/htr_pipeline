import torch

from htr_pipeline.models.model import Model


class OpenMMLabModel(Model):
    def __init__(self):
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
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

