import pandas as pd
import mlflow
import mlflow.sklearn
import joblib
import json

import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from pathlib import Path
from src.entity.config_entities import ModelEvalConfig
import dagshub

dagshub.init(repo_owner="aakash-tsx", repo_name="testing_auto_versioning", mlflow=True)


class ModelEvaluation:
    def __init__(self, config: ModelEvalConfig):
        self.config = config
        mlflow.set_tracking_uri(
            # "http://localhost:5000"
            "https://dagshub.com/aakash-tsx/testing_auto_versioning.mlflow"
        )  # Change if using remote MLflow
        mlflow.set_experiment("Model_Evaluation")

    def eval_metrics(self, actual, pred):
        return {
            "rmse": np.sqrt(mean_squared_error(actual, pred)),
            "mae": mean_absolute_error(actual, pred),
            "r2": r2_score(actual, pred),
        }

    def log_evaluation(self):
        test_data = pd.read_csv(self.config.test_data)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop(columns=[self.config.target_column])
        test_y = test_data[self.config.target_column]

        preds = model.predict(test_x)
        metrics = self.eval_metrics(test_y, preds)

        print(
            f"RMSE: {metrics['rmse']:.4f}, MAE: {metrics['mae']:.4f}, R²: {metrics['r2']:.4f}"
        )

        with mlflow.start_run():
            mlflow.log_params({"model_name": self.config.model_path})
            mlflow.log_metrics(metrics)
            mlflow.sklearn.log_model(model, "evaluated_model")

        # Save metrics locally
        Path(self.config.metric_file).write_text(json.dumps(metrics, indent=4))
