from src.config.config_manager import ConfigManager
from src.components.data_validation import DataValidation
from src.logger import logging


STAGE_NAME = "Data Validation"


class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
