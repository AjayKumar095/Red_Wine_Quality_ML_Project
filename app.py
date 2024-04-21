from common.logger import logging
import pickle
from flask import Flask, render_template, request
from src.pipeline.prediction_pipeline import PredictPipeline
app=Flask(__name__)


@app.route('/', methods=['GET', "POST"])
def homepage():
    try :
        logging.info("at home page")
        return render_template('index.html')
    except:
        return render_template('PageError.html', error=f'500 - Internal Server Error')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:
        if request.method=='GET':
           logging.info('in if block')
           return render_template('PageError.html', error=f'500 - Internal Server Error')
        else :
            
            logging.info('in else block')
            fixed_acidity=request.form.get('fixed_acidity')
            volatile_acidity=request.form.get("volatile_acidity")
            citric_acid=request.form.get('citric_acid')
            residualsugar=request.form.get('residual_sugar')
            chlorides=request.form.get('chlorides')
            free_sulfur_dioxide=request.form.get('free_sulfur_dioxide')
            total_sulfur_dioxide=request.form.get('total_sulfur_dioxide')
            density=request.form.get('density')
            pH=request.form.get('pH')
            sulphates=request.form.get('sulphates')
            alcohol=request.form.get('alcohol')
            
            values=[[fixed_acidity, volatile_acidity, citric_acid, residualsugar, chlorides, free_sulfur_dioxide, 
                    total_sulfur_dioxide, density, pH, sulphates, alcohol]]
            
            logging.info(f'valuse {str(values)}')
            
            logging.info('calling pipeline')
            model=PredictPipeline()
            logging.info('predicting')
            y_pred=model.Predict(values)
            
            logging.info(f'quality rank app.py = {y_pred}')
            
            quality_rank=int(y_pred)
            logging.info(f"quality rank {quality_rank}")
            
        
            return render_template('index.html', Quailty=quality_rank)
    except:
        return render_template('PageError.html', error=f'500 - Internal Server Error')


if __name__ == '__main__':
    
    app.run(debug=True, port=5000)