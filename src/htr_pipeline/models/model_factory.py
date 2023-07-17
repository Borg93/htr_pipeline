from htr_pipeline.models.region.rmdet_region import RmtDetRegion
from htr_pipeline.models.transcribe.trocr import TrOCR


class ModelFactory:
    def __init__(self):
        self.models = {
            'RmtDetRegion': RmtDetRegion,
            # 'LineModel': LineModel,
            # 'TranscriberModel': TranscriberModel,
            # Add more as needed
        }

    def create(self, model_name):
        if model_name not in self.models:
            raise ValueError(f"Unknown model name: {model_name}")

        model = self.models[model_name]()
        model.load_model()  # Make sure to load the model as well
        return model
