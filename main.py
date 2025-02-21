from src.pipeline.s01_data_ingestion import DataIngestionPipeline
from src.pipeline.s02_data_validation import DataValidationPipeline
from src.pipeline.s03_data_transformation import DataTransformationPipeline
from src.pipeline.s04_model_trainer import ModelTrainerPipeline
from src.pipeline.s05_model_eval import ModelEvaluationPipeline
from src.logger import logging


STAGE_NAME = "Data Ingestion stage"
try:
    logging.info(f"          {STAGE_NAME} Initiated...")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logging.info(f"          {STAGE_NAME} Completed...")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
    logging.info(f"          {STAGE_NAME} Initiated...")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.main()
    logging.info(f"          {STAGE_NAME} Completed...")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"
try:
    logging.info(f"          {STAGE_NAME} Initiated...")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.main()
    logging.info(f"          {STAGE_NAME} Completed...")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Model Training"
try:
    logging.info(f"          {STAGE_NAME} Initiated...")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.main()
    logging.info(f"          {STAGE_NAME} Completed...")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"
try:
    logging.info(f"          {STAGE_NAME} Initiated...")
    model_eval_pipeline = ModelEvaluationPipeline()
    model_eval_pipeline.main()
    logging.info(f"          {STAGE_NAME} Completed...")
except Exception as e:
    raise e
