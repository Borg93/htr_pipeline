from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def predict(self, input_data):
        pass

    @abstractmethod
    def get_model_type(self):
        pass

# perhaps should be simlair as the strategy with inthertiance of model_type?

