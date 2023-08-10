from htr.inferencer.inferencers.region_inferencer import RegionInferencer


class InferencerFactory:
    def __init__(self):
        self.inferencers = {
            RegionInferencer.inferencer_type: RegionInferencer,
            # ... other inferencers
        }

    def create_inferencer(self, model, preprocessing_strategies, postprocessing_strategies):
        model_type = model.model_type

        if model_type not in self.inferencers:
            raise ValueError(f"Unknown model type: {model_type}")

        return self.inferencers[model_type](model, preprocessing_strategies, postprocessing_strategies)
