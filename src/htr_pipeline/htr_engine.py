import logging

from config_manager import ConfigManager
from inference_loader import InferencerLoader
from inferencer.inferencer import InferencerProtocol


# TODO - option to load from the hub and local.
# IDEA : We should be able to pass a model but additonal configurations as strategies and type of inferencer it was should be able to be saved and seralized 
# and be push to the hub. Perhaps simlair as bertopic implmetnation?

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

    def load_inferencer(self, folder_path):
        self.inferencer_loader.load(folder_path)

    def register_custom_strategy(self, strategy_type, strategy_name, strategy_class):
        strategy_factory = self.inferencer_loader._get_strategy_factory(strategy_type)
        strategy_factory.register_custom_strategy(strategy_name, strategy_class)

    def register_custom_model():
        raise NotImplementedError("The method to load custom models not implemented yet, should be simlair as register_custom_strategy.")

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
    engine.register_custom_strategy("preprocessing", "custom_binarize", CustomBinarize)
