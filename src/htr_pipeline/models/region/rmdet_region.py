
from htr_pipeline.models.model import Model


class RmtDetRegion(Model):
    def __init__(self, model_name):
        super().__init__(model_name)

    def preprocess(self, input):
        # Implement preprocessing specific to ModelA
        pass

    def postprocess(self, raw_output):
        # Implement postprocessing specific to ModelA
        pass

    def predict(self, input):
        # Implement prediction logic specific to ModelA
        pass

    def load_model(self):
        # Load model specifics
        pass

    def get_model_type(self):
        return 'region'
