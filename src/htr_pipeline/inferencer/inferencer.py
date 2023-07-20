from abc import ABC, abstractmethod
from typing import Any, Protocol


class Inferencer(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def inferencer_type(self):
        pass

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

# TODO update types..
class InferencerProtocol(Protocol):
    def preprocess(self, input_image: Any) -> Any:
        ...

    def predict(self, preprocessed: Any) -> Any:
        ...

    def postprocess(self, raw_output: Any) -> Any:
        ...

    def visualize(self, raw_output: Any) -> None:
        ...