import os
import urllib.request as request
import pandas as pd
from sklearn.model_selection import train_test_split
from src.entity.config_entities import DataTransformationConfig
from src.logger import logging


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logging.info(f"Splitted data into TRAIN and TEST set at {self.config.root_dir}")
        logging.info(train.shape)
        logging.info(test.shape)
