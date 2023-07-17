import json
import logging

from .inferencer.inferencer_factory import InferencerFactory
from .models.model_factory import ModelFactory


class HTREngine:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.inferencers = {}
        self.model_factory = ModelFactory()
        self.inferencer_factory = InferencerFactory()

    def load_model(self, config_file_path):
        try:
            with open(config_file_path, 'r') as config_file:
                config = json.load(config_file)

            model_name = config.get('model_name')
            model_type = config.get('model_type')

            if not model_name or not model_type:
                raise ValueError("Both 'model_name' and 'model_type' must be specified in the configuration file.")

            model = self.model_factory.create(model_name)

            if model.get_model_type() != model_type:
                raise ValueError(f"The model {model_name} does not match the specified model type {model_type}.")

            self.inferencers[model_type] = self.inferencer_factory.create(model)
        except Exception as e:
            logging.error(f"Failed to load model: {str(e)}")

    def run_inference(self, inferencer_key, input_image):
        return self._run_inferencer(inferencer_key, input_image)

    def _run_inferencer(self, inferencer_key, input_image):
        try:
            preprocessed = self.inferencers[inferencer_key].preprocess(input_image)
            raw_output = self.inferencers[inferencer_key].predict(preprocessed)
            processed_output = self.inferencers[inferencer_key].postprocess(raw_output)
            self.inferencers[inferencer_key].visualize()
            return processed_output
        except Exception as e:
            logging.error(f"Failed to run {inferencer_key} inferencer: {str(e)}")

if __name__ == "__main__":
    engine = HTREngine()
    engine.load_model('config_rmtdet.json')
    # result = engine.run_inference('region', input_image)
