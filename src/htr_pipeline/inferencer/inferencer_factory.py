from .region_inferencer import RegionInferencer


class InferencerFactory:
    def __init__(self):
        self.inferencers = {
            'region': RegionInferencer,
            # 'line': LineInferencer,
            # 'transcriber': TranscriberInferencer,
            # add more as needed
        }

    def create(self, model, preprocessing_strategies, postprocessing_strategies):
        model_type = model.get_model_type()

        if model_type not in self.inferencers:
            raise ValueError(f"Unknown model type: {model_type}")

        return self.inferencers[model_type](model, preprocessing_strategies, postprocessing_strategies)
