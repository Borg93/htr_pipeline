import os

from htr.enums import ModelName, ModelType
from htr.models.model import Model


class RmtDetRegionConfig:
    # Define your configuration fields here.
    pass

class RmtDetRegion(Model):
    def __init__(self, config: RmtDetRegionConfig):
        self._model_type = ModelType.REGION.value
        self._model_name = ModelName.RMT_DET_REGION.value

    @property
    def model_type(self):
        return self._model_type

    @property
    def model_name(self):
        return self._model_name

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

    def load_model(self, folder_path):
        # model_file_path = os.path.join(folder_path, 'model.pth')
        # self.model = torch.load(model_file_path)

        print(f"Model loaded: {self.model_name} from 'model_file_path'")