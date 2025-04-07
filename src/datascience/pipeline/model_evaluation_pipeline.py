from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            # model_evaluation.evaluate_model()
            model_evaluation.log_to_mlflow()
        except Exception as e:
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<\n\nx=====x")
    except Exception as e:
        logger.exception(e)
        raise e