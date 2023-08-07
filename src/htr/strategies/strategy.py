from abc import ABC, abstractmethod


class Strategy(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def strategy_name(self):
        pass

    @property
    @abstractmethod
    def strategy_type(self):
        pass

    @abstractmethod
    def process(self, input_image):
        pass
