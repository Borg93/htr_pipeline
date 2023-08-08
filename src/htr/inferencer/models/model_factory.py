from htr.enums import ModelName
from htr.inferencer.models.base_model import Model
from htr.inferencer.models.region.rmdet_region import RmtDetRegion


class ModelFactory:
    def __init__(self):
        self.models = {
            ModelName.RMT_DET_REGION.value: RmtDetRegion,
            # Add more as needed
        }

    def register_custom_model(self, model_name, model_type, model_class):
        if not issubclass(model_class, Model):
            raise TypeError("model_class must be a subclass of Model.")
        self.models[model_name] = model_class

    def create(self, model_name, model_type, config_data):
        model_class = self.models.get(model_name)
        if not model_class:
            raise ValueError(f"Invalid model name: {model_name}")

        model = model_class(config_data)
        if model.model_type != model_type:
            raise ValueError(f"Model type mismatch: model {model_name} is not of type {model_type}")

        model.load_model(config_data)

        return model
