from abc import ABC, abstractmethod

from huggingface_hub import ModelHubMixin


class Model(ModelHubMixin,ABC):
    def __init__(self, config_data):
        self.config_data = config_data

    @property
    @abstractmethod
    def model_name(self):
        pass

    @property
    @abstractmethod
    def model_type(self):
        pass

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