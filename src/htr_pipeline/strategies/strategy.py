from abc import ABC, abstractmethod


class Strategy(ABC):
    def __init__(self, strategy_type):
        self.strategy_type = strategy_type

    @abstractmethod
    def process(self, input_image):
        pass
