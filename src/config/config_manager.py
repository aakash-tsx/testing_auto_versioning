from pathlib import Path
from src.utils.common import read_yaml, create_directories
from src.entity.config_entities import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvalConfig,
)
from src.constants import *


class ConfigManager:
    def __init__(
        self,
        config_path=CONFIG_FILE_PATH,
        params_path=PARAMS_FILE_PATH,
        schema_path=SCHEMA_FILE_PATH,
    ):

        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        self.schema = read_yaml(schema_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        data_ingestion_config_details = self.config.data_ingestion

        create_directories([data_ingestion_config_details.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=data_ingestion_config_details.root_dir,
            source_url=data_ingestion_config_details.source_url,
            download_zip_file_dir=data_ingestion_config_details.download_zip_file_dir,
            unzip_zipped_file_dir=data_ingestion_config_details.unzip_zipped_file_dir,
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        data_validation_config_details = self.config.data_validation
        data_validation_schema_details = self.schema.COLUMNS

        create_directories([data_validation_config_details.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=data_validation_config_details.root_dir,
            unzip_data_dir=data_validation_config_details.unzip_data_dir,
            status_file=data_validation_config_details.status_file,
            all_schema=data_validation_schema_details,
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        data_transformation_config_details = self.config.data_transformation

        create_directories([data_transformation_config_details.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=data_transformation_config_details.root_dir,
            data_path=data_transformation_config_details.data_path,
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        model_trainer_config_details = self.config.model_trainer
        model_trainer_params_details = self.params.ElasticNet
        model_trainer_schema_details = self.schema.TARGET_COLUMN

        create_directories([model_trainer_config_details.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=model_trainer_config_details.root_dir,
            train_data=model_trainer_config_details.train_data,
            test_data=model_trainer_config_details.test_data,
            model_name=model_trainer_config_details.model_name,
            alpha=model_trainer_params_details.alpha,
            l1=model_trainer_params_details.l1,
            target_column=model_trainer_schema_details.name,
        )

        return model_trainer_config

    def get_model_eval_config(self) -> ModelEvalConfig:
        model_eval_config_details = self.config.model_evaluation
        model_eval_params_details = self.params.ElasticNet
        model_eval_schema_details = self.schema.TARGET_COLUMN

        create_directories([model_eval_config_details.root_dir])

        model_eval_config = ModelEvalConfig(
            root_dir=model_eval_config_details.root_dir,
            test_data=model_eval_config_details.test_data,
            model_path=model_eval_config_details.model_path,
            metric_file=model_eval_config_details.metric_file,
            all_params=model_eval_params_details,
            target_column=model_eval_schema_details.name,
            mlflow_uri="http://localhost:5000",
        )

        return model_eval_config
