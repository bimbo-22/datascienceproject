import os
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from urllib.parse import urlparse
from src.datascience import logger
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.datascience.entity.config_entity import ModelEvaluationConfig
from pathlib import Path
from src.datascience.utils.common import save_json

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/bimbo-22/datascienceproject.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "bimbo-22"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "password"

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def evaluate_model(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        r2 = r2_score(actual, pred)
        mae = mean_absolute_error(actual, pred)
        return rmse, r2, mae

    def log_to_mlflow(self):
        
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        x_test = test_data.drop(columns=[self.config.target_column], axis = 1)
        y_test = test_data[self.config.target_column]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            
            predicted_qualities = model.predict(x_test)
            (rmse, r2, mae) = self.evaluate_model(y_test, predicted_qualities)
            
            # save metrics locally
            scores = {
                "rmse": rmse,
                "r2": r2,
                "mae": mae
            }
            
            save_json(path=Path(self.config.metric_file_name), data=scores)
            
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)
            
            # model registry dosen't support local file system 
            if tracking_uri_type_store != "file":
                mlflow.sklearn.log_model(model, registered_model_name="ElasticNet", artifact_path="model")
            else:
                mlflow.sklearn.log_model(model, artifact_path="model")