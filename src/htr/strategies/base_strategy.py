from abc import ABC, abstractmethod


class Strategy(ABC):
    strategy_type = None

    def __init__(self):
        pass

    @property
    def name(self):
        return self.__class__.__name__

    @property
    @abstractmethod
    def strategy_type(self):
        pass

    @abstractmethod
    def process(self, input_image):
        pass


class PreProcessing(Strategy):
    strategy_type = "preprocessing"


class PostProcessing(Strategy):
    strategy_type = "postprocessing"
