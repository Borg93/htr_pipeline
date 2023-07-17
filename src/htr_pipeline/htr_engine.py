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
            config = self.config_manager.read(config_file_path)
            model_name = config['model_name']
            model = self.model_factory.create(model_name)

            preprocessing_strategies = []
            if 'preprocessing' in config:
                for strategy in config['preprocessing']:
                    preprocessing_strategies.append(self.preprocessing_strategy_factory.create(strategy))

            postprocessing_strategies = []
            if 'postprocessing' in config:
                for strategy in config['postprocessing']:
                    postprocessing_strategies.append(self.postprocessing_strategy_factory.create(strategy))

            inferencer = self.inferencer_factory.create(model, preprocessing_strategies, postprocessing_strategies)
            model_type = model.get_model_type()
            self.inferencers[model_type] = inferencer
        except Exception as e:
            logging.error(f"Failed to load model: {str(e)}")


    def run_inference(self, model_type, input_image):
        return self._run_inferencer(model_type, input_image)

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
    engine.run_inference('region', 'input_image.png')
