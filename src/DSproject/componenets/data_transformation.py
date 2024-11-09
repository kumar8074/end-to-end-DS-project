import os
from src.DSproject import logger
from sklearn.model_selection import train_test_split
import pandas as pd

from src.DSproject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config=config
  
    # Note: You can add different data transformation techniques such as scalar, PCA and all
  
  
    def train_test_spliting(self):
        data=pd.read_csv(self.config.data_path)
        
        # Split the data into training and test sets
        train, test=train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)