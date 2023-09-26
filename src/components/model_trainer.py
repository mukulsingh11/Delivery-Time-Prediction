from src.components import *
import os,sys
import numpy as np
import pandas as pd
from  src.logger import logging
from src.exception import CustomException

from src.config.configuration import *
from dataclasses import dataclass
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.utils import evaluate_models,save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = MODEL_FILE_PATH

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def inititate_model_tranier(self,tarin_array , test_array):
        try:
            logging.info(' we are split in data in form of dependent and independent ')

            X_train,y_train,X_test,y_test = (tarin_array[:,:-1],tarin_array[:,-1],
                                             test_array[:,:-1],test_array[:,-1])
            
            models  = {
                'XGBRegeressor': XGBRegressor(),
                'DecisionTreeRegressor' : DecisionTreeRegressor(),
                'GradientBoostingRegressor' : GradientBoostingRegressor(),
                'SVR' : SVR()

            }

            model_report:dict = evaluate_models(X_train,y_train,X_test,y_test,models)
            print(model_report)

            logging.info('sort the value of  model accuracy')
            best_model_score = max(sorted(model_report.values()))


            logging.info("sorted with model name and score value")
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            print(f"Best Model Found , Model Name : {best_model_name}, r2_Score : {best_model_score}")

            logging.info(f"Best Model Found , Model Name : {best_model_name}, r2_Score : {best_model_score}")

            save_object(file_path=self.model_trainer_config.trained_model_file_path,
                        obj=best_model)
            logging.info(f"Model training is completed")
        except Exception as e:
            raise CustomException(e,sys)
