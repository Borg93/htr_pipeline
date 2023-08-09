from htr.enums import ModelName
from htr.models.base_model import Model
from htr.models.region.rmdet_region import RmtDetRegion


class ModelFactory:
    def __init__(self):
        self.models = {
            ModelName.RMT_DET_REGION.value: RmtDetRegion,
            # Add more as needed
        }
        self._model_instances = {}  # Cache for instantiated models


    # TODO this should somehow consider model_type and if it accepted in the inferencer (e.g. region)
    def register_custom_model(self, model_name, model_type, model_class):
        if not issubclass(model_class, Model):
            raise TypeError("model_class must be a subclass of Model.")

        # if model_class.model_type != model_type:
        #     raise ValueError(f"Custom model type mismatch: model {model_name} is not of type {model_type}")

        self.models[model_name] = model_class

    def create(self, model_name, model_type, config_data):

        # Check if the model is already instantiated
        if model_name in self._model_instances:
            return self._model_instances[model_name]

        model_class = self.models.get(model_name)
        if not model_class:
            raise ValueError(f"Invalid model name: {model_name}")

        model = model_class(config_data)
        if model.model_type != model_type:
            raise ValueError(f"Model type mismatch: model {model_name} is not of type {model_type}")

        model.load_model(config_data)

        return model