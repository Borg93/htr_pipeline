from abc import ABC, abstractmethod

from huggingface_hub import ModelHubMixin


class Model(ModelHubMixin, ABC):
    @abstractmethod
    def preprocess(self, input):
        pass

    @abstractmethod
    def predict(self, input):
        pass

    @abstractmethod
    def postprocess(self, raw_output):
        pass


     # Implement the required methods for the mixin
    def _save_pretrained(self, save_directory, **kwargs):
        pass  # Implement the logic to save your model's state here

    @classmethod
    def _from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        pass  # Implement the logic to load your model's state here
