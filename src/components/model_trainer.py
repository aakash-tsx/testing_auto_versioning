import os
import joblib
import pandas as pd
from sklearn.linear_model import ElasticNet
from src.utils.common import get_size
from src.entity.config_entities import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data)

        train_x = train_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]

        lr = ElasticNet(
            alpha=self.config.alpha, l1_ratio=self.config.l1, random_state=42
        )
        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
