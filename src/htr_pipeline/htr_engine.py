import logging

from .config_manager import ConfigManager
from .inferencer.inferencer_factory import InferencerFactory
from .models.model_factory import ModelFactory
from .strategies.strategy_factory import PostprocessingStrategyFactory, PreprocessingStrategyFactory


class HTREngine:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.inferencers = {}
        self.config_manager = ConfigManager()
        self.model_factory = ModelFactory()
        self.inferencer_factory = InferencerFactory()
        self.preprocessing_strategy_factory = PreprocessingStrategyFactory()
        self.postprocessing_strategy_factory = PostprocessingStrategyFactory()

    def load_model(self, config_file_path):
        try:
            self.config_manager.read(config_file_path)
            model_name = self.config_manager.get('model_name')

            # Check if we already have an inferencer for this configuration
            if model_name in self.inferencers:
                logging.info(f"Configuration for model {model_name} already loaded, reusing existing inferencer.")
                return

            model_type = self.config_manager.get('model_type')
            model = self.model_factory.create(model_name, model_type)


            preprocessing_strategies = self._create_strategies('preprocessing')
            postprocessing_strategies = self._create_strategies('postprocessing')

            inferencer = self.inferencer_factory.create(model, preprocessing_strategies, postprocessing_strategies)
            self.inferencers[model_name] = inferencer
        except Exception as e:
            logging.error(f"Failed to load model: {str(e)}")

    def _create_strategies(self, strategy_type):
        strategy_factory = self.preprocessing_strategy_factory if strategy_type == 'preprocessing' else self.postprocessing_strategy_factory
        strategy_config = self.config_manager.get(strategy_type)
        return [strategy_factory.create(strategy, strategy_type) for strategy in strategy_config] if strategy_config else []

    def run_inference(self, model_name, input_image):
        return self._run_inferencer(model_name, input_image)

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


if __name__ == "__main__":
    engine = HTREngine()
    engine.load_model('config_rmtdet.json')
    engine.run_inference('region', 'input_image.png')
