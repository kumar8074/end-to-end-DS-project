from src.DSproject import logger
from src.DSproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.DSproject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage{STAGE_NAME} started <<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME="Data Validation Stage"

try:
    logger.info(f">>>>>> stage{STAGE_NAME} started <<<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


