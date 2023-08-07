
from htr.models.openmmlab.openmmlab_model import OpenMMLabModel


class RmtDetRegion(OpenMMLabModel):
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

