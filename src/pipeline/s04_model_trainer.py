from src.config.config_manager import ConfigManager
from src.components.model_trainer import ModelTrainer
from src.logger import logging


STAGE_NAME = "Data Model Trainer"


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
