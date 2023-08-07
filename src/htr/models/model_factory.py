from htr.enums import ModelType
from htr.models.model import Model
from htr.models.region.rmtDet_region import RmtDetRegion


class ModelFactory:
    def __init__(self):
        self.models = {
            ModelType.RMTDET.value: RmtDetRegion,
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

        model = model_class()
        if model.model_type != model_type:
            raise ValueError(f"Model type mismatch: model {model_name} is not of type {model_type}")

        model.load_model(config_data)

        return model
