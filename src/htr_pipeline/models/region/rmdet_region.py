
import os

from htr_pipeline.enums import ModelFormat, ModelName, ModelType
from htr_pipeline.models.model import Model


class RmtDetRegion(Model):
    def __init__(self):
        pass

    @property
    def model_type(self):
        return ModelType.REGION.value

    @property
    def model_name(self):
        return ModelName.RMT_DET_REGION.value

    def preprocess(self, input):
        # Implement preprocessing specific to ModelA
        pass

    def postprocess(self, raw_output):
        # Implement postprocessing specific to ModelA
        pass

    def predict(self, input):
        # Implement prediction logic specific to ModelA
        print("Model region predict")
        return "prediction from rmtdet_region"

    def load_model(self, config_data):
        # model_file_path = os.path.join(folder_path, ModelFormat.PYTORCH.value)
        # self.model = torch.load(model_file_path)

        print(f"Model loaded: {self.model_name} from config.json with: {config_data}")
