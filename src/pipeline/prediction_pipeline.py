import os
import pandas as pd
from common.logger import logging
from common.utility import load_obj



class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts', 'model', 'preprocessor.pkl')
            model_path=os.path.join('artifacts','model', 'Red_Wine_ML_Model.pkl')

            preprocessor=load_obj(preprocessor_path)
            model=load_obj(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
          
col=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol', 'quality']       
class CustomData:
    def __init__(self,
                 fixed_acidity:float,
                 volatile_acidity:float,
                 citric_acid:float,
                 residual_sugar:float,
                 chlorides:float,
                 free_sulfur_dioxide:float,
                 total_sulfur_dioxide:float,
                 density:float,
                 pH:float,
                 sulphates:float,
                 alcohol:float):
        
        self.fixed_acidity=fixed_acidity
        self.volatile_acidity=volatile_acidity
        self.citric_acid=citric_acid
        self.residual_sugar=residual_sugar
        self.chlorides=chlorides
        self.free_sulfur_dioxide=free_sulfur_dioxide
        self.total_sulfur_dioxide=total_sulfur_dioxide
        self.density = density
        self.pH = pH
        self.sulphates = sulphates
        self.alcohol=alcohol

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'fixed_acidity':[self.fixed_acidity],
                'volatile_acidity':[self.volatile_acidity],
                'citric_acid':[self.citric_acid],
                'residual_sugar':[self.residual_sugar],
                'chlorides':[self.chlorides],
                'free_sulfur_dioxide':[self.free_sulfur_dioxide],
                'total_sulfur_dioxide':[self.total_sulfur_dioxide],
                'density':[self.density],
                'pH':[self.pH],
                'sulphates':[self.sulphates],
                'alcohol':[self.alcohol]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            


