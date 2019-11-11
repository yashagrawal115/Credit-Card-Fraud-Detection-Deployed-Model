# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:07:26 2019

@author: YASHA
"""

from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.externals import joblib
app = Flask(__name__)
@app.route('/a')
def test():
    return "Flask is being used for Development  today"


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            Time = float(request.form['Time'])
            V1 =  float(request.form['V1'])
            V2 =  float(request.form['V2'])
            V3 =  float(request.form['V3'])
            V4 =  float(request.form['V4'])
            V5 =  float(request.form['V5'])
            V6 =  float(request.form['V6'])
            V7 =  float(request.form['V7'])
            V8 =  float(request.form['V8'])
            V9 =  float(request.form['V9'])
            V10 =  float(request.form['V10'])
            V11 =  float(request.form['V11'])
            V12 =  float(request.form['V12'])
            V13 =  float(request.form['V13'])
            V14 =  float(request.form['V14'])
            V15 =  float(request.form['V15'])
            V16 =  float(request.form['V16'])
            V17 =  float(request.form['V17'])
            V18 =  float(request.form['V18'])
            V19 =  float(request.form['V19'])
            V20 =  float(request.form['V20'])
            V21 =  float(request.form['V21'])
            V22 =  float(request.form['V22'])
            V23 =  float(request.form['V23'])
            V24 =  float(request.form['V24'])
            V25 =  float(request.form['V25'])
            V26 =  float(request.form['V26'])
            V27 =  float(request.form['V27'])
            V28 =  float(request.form['V28']) 
            Amount = float(request.form['Amount']) 
            # Now we will create the list inorder to pass the value to the model
            pred_args = [Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, \
                         V12, V13, V14, V15, V16, V17, V18, V19,V20, V21, V22,\
                         V23, V24, V25, V26, V27, V28, Amount]
            pred_agrs_arr = np.array(pred_args)
            pred_agrs_arr = pred_agrs_arr.reshape(1,-1)
            ml_rdm_frt = open("Random_forest.pkl", "rb") 
            ml_model = joblib.load(ml_rdm_frt)
            model_prediction = ml_model.predict(pred_agrs_arr)
            model_prediction = int(model_prediction)
        except ValueError:
            return "Please check if the values are entered correctly"
    return render_template('predict.html', prediction = model_prediction)
        
if __name__ == '__main__':
    app.run()
    
    
    