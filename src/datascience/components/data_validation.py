import pandas as pd
import os
from src.datascience import logger
from src.datascience.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            
            data = pd.read_csv(self.config.unzip_dir)
            all_cols = list(data.columns)
            all_types = list(data.dtypes)
            
            
            all_schema = self.config.all_schema.keys()
            all_schema_types = self.config.all_schema.values()
            
            for col in all_cols:
                for type_ in all_types:
                    if col not in all_schema and type_ not in all_schema_types:
                        validation_status = False
                        with open(self.config.STATUS_FILE, 'w') as file:
                            file.write(f"Validation status: {validation_status}\n")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as file:
                        file.write(f"Validation status: {validation_status}\n")
            return validation_status
        except Exception as e:
            raise e