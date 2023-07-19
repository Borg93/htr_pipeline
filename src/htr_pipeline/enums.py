from enum import Enum


class ConfigKey(Enum):
    MODEL_NAME = 'model_name'
    MODEL_HF = 'model_hf'
    MODEL_TYPE = 'model_type'
    PREPROCESSING = 'preprocessing'
    POSTPROCESSING = 'postprocessing'
    VERBOSE = 'verbose'


class InferencerType(Enum):
    REGION = "region"
    # LINE = "line"
    # TRANSCRIBER = "transcriber"
    # add other inferencer names as needed


class ModelType(Enum):
    REGION = "region"
    # add other model types as needed


class ModelName(Enum):
    RMT_DET_REGION = "RmtDetRegion"
    TR_OCR = "TrOCR"
    # add other model names as needed


class StrategyType(Enum):
    PREPROCESSING = 'preprocessing'
    POSTPROCESSING = 'postprocessing'


class StrategyName(Enum):
    SIMPLE_BINARIZE = "simplebinarize"
    SIMPLE_POSTPROCESSING = "simplepost"
    # add other strategy names as needed





