from flask import Flask, jsonify, request
import pickle
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

with open("prepline.pkl", "rb") as f:
    prepline = pickle.load(f)

model = load_model('tensormodel.h5')

columns = [
    'gender',
    'SeniorCitizen',
    'Partner',
    'Dependents',
    'Contract',
    'PaperlessBilling',
    'PaymentMethod',
    'MultipleLines',
    'InternetService',
    'tenure',
    'MonthlyCharges'
]

classes = ['keep', 'stop']

@app.route("/", methods=['GET','POST'])
def model_prediction():
    if request.method == "POST":
        content = request.json
        try:
            data= [content['gender'],
                   content['SeniorCitizen'],
                   content['Partner'],
                   content['Dependents'],
                   content['Contract'],
                   content['PaperlessBilling'],
                   content['PaymentMethod'],
                   content['MultipleLines'],
                   content['InternetService'],
                   content['tenure'],
                   content['MonthlyCharges']]
            data = pd.DataFrame([data], columns=columns)
            data_transformed = prepline.transform(data)
            res = model.predict(data_transformed)
            res = np.where(res[0] > 0.5, 1, 0)
            response = {"code": 200, "status":"OK", 
                        "result":{"prediction":str(res[0].item()),
                                   "description":classes[res[0].item()]}}
            return jsonify(response)
        except Exception as e:
            response = {"code":500, "status":"ERROR", 
                        "result":{"error_msg":str(e)}}
            return jsonify(response)
    return "<p>Please insert your data in frontend side.</p>"