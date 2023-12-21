from flask import Flask, request
from helpers import response, ba3s, dataSources as ba3Sources, batteryImage, find
from flask_cors import CORS
from datetime import datetime
from random import randrange
from operator import itemgetter
import model

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get("/batteries")
def batteries():
    return response(ba3s, "Batteries fetch successfully")


@app.get("/batteries/<id>")
def batteryById(id):
    return response(find(lambda item: item['id'] == int(id), ba3s), "Battery with id " + id + " fetched successfully!")


@app.post("/batteries")
def createBatteryDigitalTwin():
    name, source, description = itemgetter(
        'name', 'source', 'description')(request.json)
    newBa3 = {
        'id': len(ba3s) + 1,
        'name': name,
        'dataSource': source,
        'createdAt': datetime.now().isoformat(),
        'description': description,
        'image': batteryImage,
        'chargeCycles': randrange(1, 67),
    }
    ba3s.append(newBa3)

    return response(newBa3, "Battery Created Successfully")


@app.post("/batteries/predict")
def predictBattery():
    payloadDict = request.json

    prediction = {
        "soc": randrange(1, 100),
        "soh": randrange(1, 100),
        "createdAt": datetime.now().isoformat(),
        "batteryId": payloadDict['batteryId'],
        "chargeCycles": payloadDict['chargeCycles'],
    }

    return response(prediction, "Prediction Successful")


@app.get("/batteries/predictions")
def getPredictions():
    batteryId, minChargeCycle, maxChargeCycle, step = itemgetter(
        'batteryId', 'minChargeCycle', 'maxChargeCycle', 'step')(dict(request.args))

    predictions = model.getPredictions(
        batteryId, minChargeCycle, maxChargeCycle, step)

    return response(predictions, "Predictions fetched successfully")


# physical battery data sources


@app.get("/data-sources")
def dataSources():
    # print({'ba3Sources': ba3Sources})
    return response(ba3Sources)
