from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from common.utility import save_obj
from common.logger import logging
from dataclasses import dataclass
import os

@dataclass
class ConfigModelTrainer:
    
    model_file_path=os.path.join('artifacts', 'model', 'Red_Wine_ML_Model.pkl')
    
    
class ModelTraining:
    
    def __init__(self) -> None:
        self.model_obj=ConfigModelTrainer()
        
    
    def start_model_training(self, train_array,test_array):
        
        try :
            logging.info('Model training start.')
            X_train, y_train, X_test, y_test = (
                    train_array[:,:-1],
                    train_array[:,-1],
                    test_array[:,:-1],
                    test_array[:,-1]
            )
        
            model=RandomForestClassifier(criterion='log_loss',
                                         max_depth=6,
                                         max_features='log2',
                                         n_estimators=400,
                                         oob_score=True
                                         )             
            
            
            model.fit(X_train, y_train)
            
            y_pred=model.predict(X_test)
            accuracy=accuracy_score(y_pred=y_pred, y_true=y_test)
            model_report=classification_report(y_pred=y_pred, y_true=y_test)
            
            logging.info(f'Model accuracy: {accuracy}')
            logging.info(f'Model classification report:')
            logging.info(f'{model_report}')
            
            save_obj(
                object=model,
                file_path=self.model_obj.model_file_path
            )
        
        except Exception as e:
            logging.info(f"Having some error in model training. Error:- {e}")