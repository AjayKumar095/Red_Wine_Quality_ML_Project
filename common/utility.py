## common utility functions, save_obj, load_obj, save_new_data, evaluate_model
import pickle
from common.logger import logging
from sklearn.model_selection import train_test_split
    
def save_obj(object, file_path:str)-> None:

    logging.info("Collecting object and file path")
    
    try :
        with open(file_path, 'wb') as file_obj:
           logging.info("Open pickle file to dump object data")
           pickle.dump(object, file_obj)
           logging.info("Object save successfully")
    
    except Exception as e:
        logging.info(f"Having some error to save object, Error:- {e}")
    
    
def load_obj(file_path:str):
    
    logging.info("Collecting file path")
    
    try:
        
        with open(file_path, 'rd') as file_obj:
            logging.info(f"Reading from pickle file {file_path}")
            return pickle.load(file_obj)
        
    except Exception as e:
            logging.info(f"Having some error in load object, Error:- {e}")
        


def evaluate_model(x_train, x_test, y_train, y_test, models:list):
    pass

   
                
