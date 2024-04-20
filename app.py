from common.logger import logging
from flask import Flask, render_template, request
from src.pipeline.prediction_pipeline import PredictPipeline, CustomData
app=Flask(__name__)


@app.route('/', methods=['GET', "POST"])
def homepage():
    try :
        return render_template('index.html')
    except:
        return render_template('PageError.html', error=f'500 - Internal Server Error')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:
        if request.form=='GET':
           return render_template('PageError.html', error=f'500 - Internal Server Error')
        else :
            
            
            data=CustomData(
            fixed_acidity=request.form.get('fixed_acidity'),
            volatile_acidity=request.form.get("volatile_acidity"),
            citric_acid=request.form.get('citric_acid'),
            residualsugar=request.form.get('residual_sugar'),
            chlorides=request.form.get('chlorides'),
            free_sulfur_dioxide=request.form.get('free_sulfur_dioxide'),
            total_sulfur_dioxide=request.form.get('total_sulfur_dioxide'),
            density=request.form.get('density'),
            pH=request.form.get('pH'),
            sulphates=request.form.get('sulphates'),
            alcohol=request.form.get('alcohol')
            )
            #values=[[fixed_acidity, volatile_acidity, citric_acid, residualsugar, chlorides, free_sulfur_dioxide, 
                    #total_sulfur_dioxide, density, pH, sulphates, alcohol]]
        
        
            new_df=data.get_data_as_dataframe()
            predict_pipeline=PredictPipeline()
            prediction=predict_pipeline.predict(new_df)
        
            
        
            quality_rank=str(prediction)
        
            return render_template('index.html', Quailty=quality_rank)
    except:
        return render_template('PageError.html', error=f'500 - Internal Server Error')


if __name__ == '__main__':
    
    app.run(debug=True, port=5000)