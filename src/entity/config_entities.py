from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    download_zip_file_dir: Path
    unzip_zipped_file_dir: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    status_file: str
    all_schema: dict


@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data: Path
    test_data: Path
    target_column: str
    model_name: str
    alpha: float
    l1: float


@dataclass
class ModelEvalConfig:
    root_dir: Path
    test_data: Path
    model_path: Path
    metric_file: Path
    all_params: dict
    target_column: str
    mlflow_uri: str
