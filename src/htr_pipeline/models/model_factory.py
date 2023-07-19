from htr_pipeline.enums import ModelName
from htr_pipeline.models.region.rmdet_region import RmtDetRegion
from htr_pipeline.models.transcribe.trocr import TrOCR


class ModelFactory:
    def __init__(self):
         self.models = {
            ModelName.RMT_DET_REGION.value: RmtDetRegion,
            ModelName.TR_OCR.value : TrOCR
            # add your other models here
        }

    def create(self, model_name, model_type, folder_path):
        model_class = self.models.get(model_name)
        if not model_class:
            raise ValueError(f"Invalid model name: {model_name}")

        model = model_class()
        if model.model_type != model_type:
            raise ValueError(f"Model type mismatch: model {model_name} is not of type {model_type}")

        model.load_model(folder_path)

        return model
