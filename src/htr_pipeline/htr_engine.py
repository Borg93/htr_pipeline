import configparser
import logging

# from .inferencer.line_inferencer import LineInferencer
from .inferencer.inferencer_factory import InferencerFactory

# from .inferencer.transcriber_inferencer import TranscriberInferencer
from .models.model_factory import ModelFactory


class HTREngine:
    def __init__(self):
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.inferencers = {}

        self.model_factory = ModelFactory()
        self.inferencer_factory = InferencerFactory()

    def load_region_model(self, config_file_path):
        try:
            config = configparser.ConfigParser()
            config.read(config_file_path)
            region_model = self.model_factory.create(config)
            self.inferencers['region'] = self.inferencer_factory.create(region_model)
        except Exception as e:
            logging.error(f"Failed to load region model: {str(e)}")

    def load_line_model(self, config_file_path):
        try:
            config = configparser.ConfigParser()
            config.read(config_file_path)
            line_model = self.model_factory.create(config)
            line_model = self.model_factory.create(config)
            self.inferencers['line'] = self.inferencer_factory.create(line_model)
        except Exception as e:
            logging.error(f"Failed to load line model: {str(e)}")

    def load_transcribe_model(self, config_file_path):
        try:
            config = configparser.ConfigParser()
            config.read(config_file_path)
            transcribe_model = self.model_factory.create(config)
            self.inferencers['transcriber'] = self.inferencer_factory.create(transcribe_model)
        except Exception as e:
            logging.error(f"Failed to load transcriber model: {str(e)}")


    # Add set_line_model and set_transcriber_model methods similarly

    def run_region_inference(self, input_image):
        return self._run_inferencer('region', input_image)

    # Add run_line_inference and run_transcriber_inference methods similarly

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
    engine = HTREngine(config_file_path)
    engine.set_model_for_inferencer(('region', 'RmTDet'))


