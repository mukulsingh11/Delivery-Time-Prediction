import os,sys
import numpy as np
import pandas as pd
from src.constant import *
from src.config.configuration import *
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation , DataTransformationConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path:str = TRAIN_FILE_PATH
    test_data_path:str = TEST_FILE_PATH
    raw_data_path:str = RAW_FILE_PATH

class DataIngestion:
    def __init__(self):
        logging.info('******************* Data ingestion is started ***********************')
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info('********** import dataset ***********')
            df = pd.read_csv(DATASET_PATH)

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok= False)
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False)

            logging.info('train_test_split')
            train_set , test_set = train_test_split(df , test_size=0.25 , random_state=40)

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            train_set.to_csv(self.data_ingestion_config.train_data_path,header = True)

            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path),exist_ok=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path,header=True)

            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )
        
            
            


       
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    obj = DataIngestion()
    train_data , test_data = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr , test_arr,_ = data_transformation.inititate_data_transformation(train_data , test_data)
    model_trainer = ModelTrainer()
    print(model_trainer.inititate_model_tranier(train_arr,test_arr))


