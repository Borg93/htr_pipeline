import logging
from abc import ABC, abstractmethod
from typing import Any, Protocol


class Inferencer(ABC):
    inferencer_type = None

    def __init__(self, model, preprocess_strategies=None, postprocess_strategies=None):
        self.model = model
        self.preprocess_strategies = preprocess_strategies or []
        self.postprocess_strategies = postprocess_strategies or []
        self.predicted = False

        if not self.preprocess_strategies:
            logging.info(f"INFO: No preprocess strategies provided for {self.name}.")
        if not self.postprocess_strategies:
            logging.info(f"INFO: No postprocess strategies provided for {self.name}.")

    @property
    def details(self):
        return {
            "inferencer": self.name,
            "model": self.model.name,
            "preprocess_strategies": [strategy.name for strategy in self.preprocess_strategies],
            "postprocess_strategies": [strategy.name for strategy in self.postprocess_strategies],
        }

    @property
    def name(self):
        return self.__class__.__name__

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


class Region(Inferencer):
    inferencer_type = "region"


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
