import pandas as pd
import os
from src.datascience import logger
from sklearn.linear_model import ElasticNet
import joblib

from src.datascience.entity.config_entity import ModelTrainerConfig

class ModelTrainer: 
    def __init__(self, config:ModelTrainerConfig):
        self.config = config
        
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        
        x_train = train_data.drop(columns=[self.config.target_column])
        y_train = train_data[self.config.target_column]
        x_test = test_data.drop(columns=[self.config.target_column])
        y_test = test_data[self.config.target_column]
        
        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(x_train, y_train)
        
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
        logger.info("Model training completed successfully.")