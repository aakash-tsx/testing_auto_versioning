import os
import urllib.request as request
import zipfile
from src.logger import logging
from src.utils.common import get_size
from pathlib import Path
from src.entity.config_entities import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.download_zip_file_dir):
            filename, headers = request.urlretrieve(
                url=self.config.source_url, filename=self.config.download_zip_file_dir
            )
            logging.info(f"{filename} download! with following info: \n{headers}")
        else:
            logging.info(
                f"File already exists of size: {get_size(Path(self.config.download_zip_file_dir))}"
            )

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_zipped_file_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.download_zip_file_dir, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
