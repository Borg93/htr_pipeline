import logging

from htr.inferencer.base_inferencer import InferencerProtocol
from htr.inferencer.inference_loader import InferencerLoader


class HTREngine:
    def __init__(self, inferencer_loader=InferencerLoader()):
        logging.basicConfig(level=logging.INFO)
        self.inferencer_loader = inferencer_loader

    @property
    def inferencer_keys(self):
        return {key: inferencer.details for key, inferencer in self.inferencer_loader.inferencers.items()}

    def get_inferencer_details(self, inferencer_key):
        return self.inferencer_loader.get_inferencer_details(inferencer_key)

    def load_inferencer(self, key, config_data_or_path):
        self.inferencer_loader.load_inferencer(key, config_data_or_path)

    def run_inference(self, inferencer_key, input_image, visualize=False):
        return self._run_inferencer(inferencer_key, input_image, visualize)

    def _run_inferencer(self, inferencer_key, input_image, visualize):
        try:
            inferencer: InferencerProtocol = self.inferencer_loader.inferencers[inferencer_key]
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

    # def push_to_hf_hub(self):
    #     raise NotImplementedError("The method to push to the hub is not implemented yet.")

    # def load_from_hf_hub(self):
    #     raise NotImplementedError("The method to load from the hub is not implemented yet.")

    # def load_pipeline(self):
    #     raise NotImplementedError("The method to load pipeline from config is not implemented yet.")


if __name__ == "__main__":
    # Importing here to avoid circular imports

    # loader = InferencerLoader()
    # loader.register_custom_model("new_model_name", NewModelClass)
    # engine = HTREngine(loader)

    engine = HTREngine()
    engine.load_inferencer("/workspaces/htr/notebooks/RmtDet")
    # engine.run_inference('region', 'input_image.png')
