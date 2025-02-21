import os
import dagshub
import mlflow
import numpy as np
import pandas as pd
import joblib
import json
import subprocess
from pathlib import Path
from src.entity.config_entities import ModelEvalConfig
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Initialize DagsHub MLflow Tracking
dagshub.init(repo_owner="aakash-tsx", repo_name="testing_auto_versioning", mlflow=True)


class ModelEvaluation:
    def __init__(self, config: ModelEvalConfig):
        self.config = config

        # Set MLflow tracking to DagsHub
        mlflow.set_tracking_uri("https://dagshub.com/aakash-tsx/testing_auto_versioning.mlflow")
        
        mlflow.set_experiment("Model_Evaluation")

    def eval_metrics(self, actual, pred):
        return {
            "rmse": np.sqrt(mean_squared_error(actual, pred)),
            "mae": mean_absolute_error(actual, pred),
            "r2": r2_score(actual, pred),
        }

    def log_evaluation(self):
        try:
            # Load test data
            test_data = pd.read_csv(self.config.test_data)
            model = joblib.load(self.config.model_path)
            
            test_x = test_data.drop(columns=[self.config.target_column])
            test_y = test_data[self.config.target_column]

            # Make predictions
            try:
                preds = model.predict(test_x)
            except Exception as e:
                print(f"Error in model prediction: {e}")
                return

            # Compute evaluation metrics
            metrics = self.eval_metrics(test_y, preds)
            
            # Attempt to get Git commit hash
            try:
                commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode()
            except subprocess.CalledProcessError:
                commit_hash = "unknown"

            print(f"####################### Commit Hash: {commit_hash} #########################")

            # Log results to MLflow
            with mlflow.start_run() as run:
                mlflow.set_tag("mlflow.source.git.commit", commit_hash)
                mlflow.log_params(vars(self.config))  # Log all config attributes
                mlflow.log_metrics(metrics)
                mlflow.sklearn.log_model(model, "evaluated_model")

            # Save metrics locally
            Path(self.config.metric_file).write_text(json.dumps(metrics, indent=4))
            print("Model evaluation completed successfully!")
        
        except Exception as e:
            print(f"Unexpected error during model evaluation: {e}")
