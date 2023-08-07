from htr.models.huggingface.trocr import TrOCR
from htr.models.openmmlab.rmdet_region import RmtDetRegion


class ModelFactory:
    def __init__(self):
        self.factories = {
            'huggingface': HuggingFaceModelFactory(),
            'openmmlab': OpenMMLabModelFactory(),
            # add more as needed
        }

    def create(self, model_config):
        framework = model_config['framework']
        model_name = model_config['name']

        if framework not in self.factories:
            raise ValueError(f"Unknown model framework: {framework}")

        return self.factories[framework].create(model_name)


class HuggingFaceModelFactory:
    def __init__(self):
        self.models = {
            'TrOCR': TrOCR,
            # 'modelB': HuggingFaceModelB
            # add more as needed
        }
    
    def create(self, model_name):
        if model_name not in self.models:
            raise ValueError(f"Unknown HuggingFace model: {model_name}")

        return self.models[model_name](model_name)


class OpenMMLabModelFactory:
    def __init__(self):
        self.models = {
            'RmtDetRegion': RmtDetRegion,
            # 'modelB': OpenMMLabModelB
            # add more as needed
        }

    def create(self, model_name):
        if model_name not in self.models:
            raise ValueError(f"Unknown HuggingFace model: {model_name}")

        return self.models[model_name](model_name)
