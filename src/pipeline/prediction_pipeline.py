import os
import pandas as pd
from common.logger import logging
from common.utility import load_obj



class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            #preprocessor_path=os.path.join('artifacts', 'model', 'preprocessor.pkl')
            model_path=os.path.join('artifacts','model', 'Red_Wine_ML_Model.pkl')

            #preprocessor=load_obj(preprocessor_path)
            model=load_obj(model_path)

            #data_scaled=preprocessor.transform(features)

            pred=model.predict(features)
            logging.info(f'predicting quality {pred}')
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
          

            


