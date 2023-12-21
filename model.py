from datetime import datetime
from random import randrange


def getPredictions(batteryId, minChargeCyle, maxChargeCycle, step=1):
    predictions = []

    for cycle in range(int(minChargeCyle), int(maxChargeCycle), int(step)):
        prediction = {
            "soc": randrange(1, 100),
            "soh": randrange(1, 100),
            "createdAt": datetime.now().isoformat(),
            "batteryId": batteryId,
            "chargeCycles": cycle,
        }

        predictions.append(prediction)

    return predictions
