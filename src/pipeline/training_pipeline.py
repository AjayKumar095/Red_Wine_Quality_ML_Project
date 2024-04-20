from common.logger import logging
from src.components.data_intake import IntakeData
from src.components.model_trainer import ModelTraining
from src.components.data_transform import DataTransforming


if __name__=="__main__":
    
    obj=IntakeData()
    logging.info('Stat processing.')
    train_data_path, test_data_path=obj.load_data()
    logging.info('Getting the train test path.')
    
    logging.info('passing path to data transformation.')
    data_transform=DataTransforming()
    
    train_arr, test_arr,_=data_transform.start_data_transforming(train_path=train_data_path, test_path=test_data_path)
    logging.info('getting the path of transformed train and test arrays.')
    
    
    train_model=ModelTraining()
    logging.info('passing path to model training.')
    train_model.start_model_training(train_array=train_arr, test_array=test_arr)  