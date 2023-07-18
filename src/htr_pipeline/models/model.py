from abc import ABC, abstractmethod


class Model(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def model_type(self):
        pass

    @property
    @abstractmethod
    def model_name(self):
        pass

    @abstractmethod
    def predict(self, input):
        pass

    @abstractmethod
    def load_model(self):
        pass
