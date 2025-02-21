from src.config.config_manager import ConfigManager
from src.components.model_evaluation import ModelEvaluation
from src import logger

STAGE_NAME = "Model evaluation stage"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        model_evaluation_config = config.get_model_eval_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_evaluation()
