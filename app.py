from flask import Flask, request
from helpers import response
from flask_cors import CORS
from datetime import datetime
from random import randrange

app = Flask(__name__)
CORS(app)

ba3s = [
    {
      "id": 1,
      "name": 'Battery 1',
      "dataSource": 'XXXXXXXXXXXXXXXXXXXX',
      "createdAt": "2023-12-01",
    },
    {
      "id": 2,
      "name": 'Battery 2',
      "dataSource": 'XXXXXXXXXXXXXXXXXXXX',
      "createdAt": "2023-12-02",
    },
    {
      "id": 3,
      "name": 'Battery 3',
      "dataSource": 'XXXXXXXXXXXXXXXXXXXX',
      "createdAt": "2023-12-03",
    },
]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/batteries")
def batteries():
    return response(ba3s)

@app.post("/batteries/predict")
def predictBattery():
    payloadDict = request.json
    
    prediction = {
        "soc": randrange(1, 100),
        "soh": randrange(1, 100),
        "createdAt": datetime.now(),
        "batteryId": payloadDict['batteryId'],
        "chargeCycles": payloadDict['chargeCycles'],
    }
    
    return response(prediction)