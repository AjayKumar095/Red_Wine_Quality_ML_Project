import os
import numpy as np 
import pandas as pd 
from common.logger import logging
from dataclasses import dataclass
from common.utility import save_obj
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE
from sklearn.compose import ColumnTransformer 


@dataclass
class ConfigDataTransform:
    data_preprocessor_file_path:str=os.path.join('artifacts', 'model', 'preprocessor.pkl')
    
    
class DataTransforming:
    
    def __init__(self) -> None:
        self.DataTransform_config=ConfigDataTransform()
        
    
    def data_transformation_obj(self):
        
        try:
            
            logging.info('Creating data transforming object.')
            
            numerical_col=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
                            'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
                            'pH', 'sulphates', 'alcohol']
            
            pipeline=Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy='median'))
                ]
            )
            
            preprocessor=ColumnTransformer([
                ('pipeline', pipeline, numerical_col)
            ])
            
            logging.info('Data tansformaing object created.')
            return preprocessor
        
        except Exception as e:
            logging.info(f'Having some error to transform the data. Error:- {e}')    
            
    def start_data_transforming(self, train_path, test_path):
        
        try:
            logging.info('Data tansformation start.')
            
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("Read train and test data completed")
            logging.info(f'Train Dataframe Head:  \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head:  \n{test_df.head().to_string()}')
            
            logging.info("Obtaining preprocessor object.")
            preprocessor_obj=self.data_transformation_obj()
            
            target_col='quality'
            col_to_drop=['quality']
            
            ## sorting data 
            
            ## test data
            test_input_data_df=test_df.drop(columns=col_to_drop, axis=1)
            test_target=test_df[target_col]
            
            ## train data
            train_input_data_df=train_df.drop(columns=col_to_drop, axis=1)
            train_target=train_df[target_col]
            
            logging.info("Applying preprocessing object on training and test datasets")
            test_input_data_arr=preprocessor_obj.fit_transform(test_input_data_df)
            train_input_data_arr=preprocessor_obj.fit_transform(train_input_data_df)
            logging.info("Data tansformation end.")
            
            test_arr=np.c_[test_input_data_arr, np.array(test_target)]
            train_arr=np.c_[train_input_data_arr, np.array(train_target)]
            
            logging.info('Saving preprocessor pickle file.')
            save_obj(
                file_path=self.DataTransform_config.data_preprocessor_file_path,
                object=preprocessor_obj
            )
            
            return (
                #train_arr,
                #test_arr,
                self.DataTransform_config.data_preprocessor_file_path 
            )
        
        except Exception as e:
            logging.info(f'Having some error in data transforming. Error:- {e}')
            
                
check=DataTransforming()

train='artifacts/Data/train.csv'
test='artifacts/Data/test.csv'     

print(check.start_data_transforming(train_path=train, test_path=test))