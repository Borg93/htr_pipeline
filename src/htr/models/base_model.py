from abc import ABC, abstractmethod

from huggingface_hub import ModelHubMixin


class Model(ModelHubMixin, ABC):
    model_type = None

    def __init__(self, config_data):
        self.config_data = config_data

    @property
    @abstractmethod
    def model_type(self):
        pass

    @property
    def name(self):
        return self.__class__.__name__

    @abstractmethod
    def predict(self, input_data):
        pass

    @abstractmethod
    def load_model(self):
        pass

    #  # Implement the required methods for the mixin
    # def _save_pretrained(self, save_directory, **kwargs):
    #     pass  # Implement the logic to save your model's state here

    # @classmethod
    # def _from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
    #     pass  # Implement the logic to load your model's state here


class RegionModel(Model):
    model_type = "region"
