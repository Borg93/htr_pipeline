import logging

from .config_manager import ConfigManager
from .enums import ConfigKey, StrategyType
from .inferencer.inferencer_factory import InferencerFactory
from .models.model_factory import ModelFactory
from .strategies.strategy_factory import PostprocessingStrategyFactory, PreprocessingStrategyFactory


# TODO - option to load from the hub and local.
# IDEA : We should be able to pass a model but additonal configurations as strategies and type of inferencer it was should be able to be saved and seralized 
# and be push to the hub. Perhaps simlair as bertopic implmetnation?

class HTREngine:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.inferencers = {}
        self.config_manager = ConfigManager()
        self.model_factory = ModelFactory()
        self.inferencer_factory = InferencerFactory()
        self.preprocessing_strategy_factory = PreprocessingStrategyFactory()
        self.postprocessing_strategy_factory = PostprocessingStrategyFactory()

    def push_to_hf_hub():
        print("will load form the hub..")

    def load_pipeline():
        # TODO this one should load multiple models and also define their sequential
        # on how they are supposed to be build and run. 
        print("will load pipeline from config")

    def load_model(self, folder_path):

        # TODO should have simlair implmentation as bertopic? Should load from the hub or locally
        # TODO think about SOLID. Single-responsibility principle.. THis class becomes now loader and inferencer. 
        # Is there away to refactor away the setter as the config manager is validatior
        try:
            self.config_manager.read(folder_path)
            model_name = self.config_manager.get(ConfigKey.MODEL_NAME.value)
            model_type = self.config_manager.get(ConfigKey.MODEL_TYPE.value)

            inferencer_key = self.get_inferencer_key(model_name, model_type)

            # Check if we already have an inferencer for this configuration
            if inferencer_key in self.inferencers:
                logging.info(f"Configuration for model {model_name} already loaded, reusing existing inferencer.")
                return
            else:
                logging.info(f"Loading {inferencer_key}.")


            model = self.model_factory.create(model_name, model_type, folder_path)


            preprocessing_strategies = self._create_strategies(StrategyType.PREPROCESSING)
            postprocessing_strategies = self._create_strategies(StrategyType.POSTPROCESSING)

            inferencer = self.inferencer_factory.create(model, preprocessing_strategies, postprocessing_strategies)
            self.inferencers[inferencer_key] = inferencer

        except Exception as e:
            logging.error(f"Failed to load model: {str(e)}")

    def _get_inferencer_key(self, model_name, model_type):
        return f"{model_name}_{model_type}"

    @property
    def inferencer_keys(self):
        return list(self.inferencers.keys)

    def _create_strategies(self, strategy_type: StrategyType):
        strategy_factory = (PreprocessingStrategyFactory()
                            if strategy_type == StrategyType.PREPROCESSING
                            else PostprocessingStrategyFactory())
        strategy_config = self.config_manager.get(strategy_type.value)
        return [strategy_factory.create(strategy, strategy_type.value) for strategy in strategy_config] if strategy_config else []



    def run_inference(self, inferencer_key, input_image):
        return self._run_inferencer(inferencer_key, input_image)

    def _run_inferencer(self, inferencer_key, input_image, visualize=False):
        try:
            inferencer = self.inferencers[inferencer_key]
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
    engine.load_model('./RmtDet')
    engine.run_inference('region', 'input_image.png')
