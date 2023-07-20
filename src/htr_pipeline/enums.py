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


class ModelType(Enum):
    REGION = "region"


class ModelName(Enum):
    """
    add other model names as needed
    """
    RMT_DET_REGION = "RmtDetRegion"
    TR_OCR = "TrOCR"


class StrategyType(Enum):
    PREPROCESSING = 'preprocessing'
    POSTPROCESSING = 'postprocessing'


class StrategyName(Enum):
    """
    add other strategy names as needed
    """
    SIMPLE_BINARIZE = "simplebinarize"
    SIMPLE_POSTPROCESSING = "simplepost"





