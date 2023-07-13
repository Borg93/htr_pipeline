from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def preprocess(self, input):
        pass

    @abstractmethod
    def predict(self, input):
        pass

    @abstractmethod
    def postprocess(self, raw_output):
        pass
