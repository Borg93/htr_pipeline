from abc import ABC, abstractmethod


class Process(ABC):
    process_type = None

    def __init__(self):
        pass

    @property
    def name(self):
        return self.__class__.__name__

    @property
    @abstractmethod
    def process_type(self):
        pass

    @abstractmethod
    def transform(self, input_image):
        pass


class PreProcessing(Process):
    process_type = "preprocessing"


class PostProcessing(Process):
    process_type = "postprocessing"
