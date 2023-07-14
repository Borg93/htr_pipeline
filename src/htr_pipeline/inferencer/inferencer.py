from abc import ABC, abstractmethod


class Inferencer(ABC):
    def __init__(self, model):
        self.model = model
        self.predicted = False

    @abstractmethod
    def preprocess(self, input_image):
        pass

    @abstractmethod
    def predict(self, preprocessed_image):
        pass

    @abstractmethod
    def postprocess(self, raw_output):
        pass

    @abstractmethod
    def visualize(self, raw_output):
        pass
