#!flask/bin/python
from flask import Flask
from flask import request
from flask_cors import CORS

import os
from joblib import dump, load
#from xgboost import XGBClassifier

from sklearn.preprocessing import MinMaxScaler
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "open the index.html file"

@app.route('/predict/')
def predict():

    try:
        #features
        x = float(request.args.get('x'))
        y = float(request.args.get('y'))
        month = float(request.args.get('month'))
        day = float(request.args.get('day'))
        ffmc = float(request.args.get('ffmc'))
        dmc = float(request.args.get('dmc'))
        dc = float(request.args.get('dc'))
        isi = float(request.args.get('isi'))
        temp = float(request.args.get('temp'))
        rh = float(request.args.get('rh'))
        wind = float(request.args.get('wind'))
        rain = float(request.args.get('rain'))

        input_features = np.array([x, y, month, day, ffmc, dmc, dc, isi, temp, rh, wind, rain]).reshape(1, -1)
        print("got features")

        # Load from file
        model = load("estimator.joblib")
        print("loaded model")

        pred = model.predict(scaled_features)

        if(str(pred) == 1):
            return "Fire"
        else:
            return "No Fire"

        return pred
    except:
        return "no fire"

if __name__ == '__main__':
    app.run(debug=True)