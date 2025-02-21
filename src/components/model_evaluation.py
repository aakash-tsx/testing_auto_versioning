import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.entity.config_entities import ModelEvalConfig
from src.utils.common import save_json
from pathlib import Path
import json


def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


class ModelEvaluation:
    def __init__(self, config):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return {"rmse": rmse, "mae": mae, "r2": r2}

    def log_evaluation(self):
        test_data = pd.read_csv(self.config.test_data)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        predicted_qualities = model.predict(test_x)

        # Compute evaluation metrics
        metrics = self.eval_metrics(test_y, predicted_qualities)
        print(metrics["rmse"])
        print(metrics["mae"])
        print(metrics["r2"])

        # Save metrics locally
        save_json(path=Path(self.config.metric_file), data=metrics)

