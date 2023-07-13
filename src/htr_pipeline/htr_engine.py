import configparser
import logging

from .inferencer.line_inferencer import LineInferencer
from .inferencer.region_inferencer import RegionInferencer
from .inferencer.transcriber_inferencer import TranscriberInferencer
from .models.model_factory import ModelFactory
from .visualizers.visualizer_factory import VisualizerFactory


class HTREngine:
    def __init__(self, config_file_path):
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.inferencers = {}

        try:
            config = configparser.ConfigParser()
            config.read(config_file_path)

            model_factory = ModelFactory()
            visualizer_factory = VisualizerFactory()

            self.set_region_model(config['region']['model'], config['region']['visualizer'], model_factory, visualizer_factory)
            # Repeat for Line and Transcriber

        except Exception as e:
            logging.error(f"Failed to initialize HTREngine: {str(e)}")

    def set_region_model(self, model_name, visualizer_name, model_factory, visualizer_factory):
        region_model = model_factory.create(model_name)
        region_visualizer = visualizer_factory.create(visualizer_name)
        self.inferencers['region'] = RegionInferencer(region_model, region_visualizer)

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
