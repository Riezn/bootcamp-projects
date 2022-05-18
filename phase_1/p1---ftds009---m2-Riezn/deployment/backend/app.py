from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

columns = ['age', 'bmi', 'children', 'sex', 'smoker', 'region']

@app.route("/")
def home():
    return "<h1>It Works!</h1>"

@app.route("/predict", methods=['GET','POST'])
def model_prediction():
    if request.method == "POST":
        content = request.json
        try:
            data= [content['age'],
                   content['bmi'],
                   content['children'],
                   content['gender'],
                   content['smoker'],
                   content['region']]
            data = pd.DataFrame([data], columns=columns)
            res = model.predict(data)
            response = {"code": 200, "status":"OK", 
                        "result":{"prediction":res[0].round(0)}}
            return jsonify(response)
        except Exception as e:
            response = {"code":500, "status":"ERROR", 
                        "result":{"error_msg":str(e)}}
            return jsonify(response)
    return "<p>Please insert your data in FE side.</p>"