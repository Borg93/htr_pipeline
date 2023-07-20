import json
import logging
import os

from config_manager import ConfigManager
from inference_loader import InferencerLoader
from inferencer.inferencer import InferencerProtocol


class HTREngine:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.inferencers = {}
        self.config_manager = ConfigManager()
        self.inferencer_loader = InferencerLoader(self.config_manager, self.inferencers)

    @property
    def inferencer_keys(self):
        return list(self.inferencers.keys())

    def push_to_hf_hub(self):
        raise NotImplementedError("The method to push to the hub is not implemented yet.")

    def load_from_hf_hub(self):
        raise NotImplementedError("The method to load from the hub is not implemented yet.")

    def load_pipeline(self):
        raise NotImplementedError("The method to load pipeline from config is not implemented yet.")

    def load_inferencer(self, config_data_or_path):
        if isinstance(config_data_or_path, dict):
            # If the input is a dictionary
            self.inferencer_loader.load(config_data_or_path)
        elif isinstance(config_data_or_path, str):
            # If the input is a string, treat it as a folder path
            config_file_path = os.path.join(config_data_or_path, 'config.json')
            with open(config_file_path, 'r') as file:
                config_data = json.load(file)
            self.inferencer_loader.load(config_data)
        else:
            raise TypeError("config_data_or_path must be a dictionary or a path to a folder containing a 'config.json' file.")


    def run_inference(self, inferencer_key, input_image, visualize=False):
        return self._run_inferencer(inferencer_key, input_image, visualize)

    def _run_inferencer(self, inferencer_key, input_image, visualize):
        try:
            inferencer: InferencerProtocol = self.inferencers[inferencer_key]
            preprocessed = inferencer.preprocess(input_image)
            raw_output = inferencer.predict(preprocessed)
            processed_output = inferencer.postprocess(raw_output)
            if visualize:
                inferencer.visualize(raw_output)
            return processed_output
        except Exception as e:
            logging.error(f"Failed to run {inferencer_key} inferencer: {str(e)}")

    def run_pipeline(self, inferencer_keys, input_image):
        output = input_image
        for inferencer_key in inferencer_keys:
            output = self.run_inference(inferencer_key, output)
        return output


if __name__ == "__main__":
    engine = HTREngine()
    engine.load_inferencer('./RmtDet')
    engine.run_inference('region', 'input_image.png')
    engine.inferencer_loader.register_custom_strategy("preprocessing", "custom_binarize", CustomBinarize)
    engine.inferencer_loader.register_custom_model(model_name, model_class)
