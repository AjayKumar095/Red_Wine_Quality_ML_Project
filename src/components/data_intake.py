import os
import pandas as pd 
from common.logger import logging
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
class DataFilePathConfig:
    
    ## declare the file path for data.
    train_data_path: str=os.path.join('artifacts','Data', 'train.csv')
    test_data_path: str=os.path.join('artifacts','Data', 'test.csv')
    
    
class IntakeData:
    
    def __init__(self):
        self.file_path_config=DataFilePathConfig()
        
    def load_data(self):
        
        logging.info('Data intake start.')
        
        try :
            
            logging.info('Reading raw data as pandas dataframe')
            df=pd.read_csv('notebook/raw_data/Raw_Data_Red_Wine.csv')
            
            ## spliting raw data into train and test data
            
            logging.info('Performing train test split on raw data')
            train_data, test_data=train_test_split(df, random_state=42, test_size=0.30)
            
            ## saving train test data to csv file
            
            train_data.to_csv(self.file_path_config.train_data_path, index=False, header=True)
            test_data.to_csv(self.file_path_config.test_data_path, index=False, header=True)
            
            logging.info("Data splite and save successfully.")
            
            return (
                
                ## returning the file path of the train and test data.
                self.file_path_config.train_data_path,
                self.file_path_config.test_data_path
            )
        
        except Exception as e:
            logging.info(f"Having some error to save files, Error:- {e}")    
            


                   