from datetime import datetime
from random import uniform


def getPredictions(batteryId, minChargeCyle, maxChargeCycle, step=1):
    predictions = []
    soc = uniform(95, 100)
    soh = uniform(95, 100)

    for cycle in range(int(minChargeCyle), int(maxChargeCycle), int(step)):
        prediction = {
            "soc": soc,
            "soh": soh,
            "createdAt": datetime.now().isoformat(),
            "batteryId": batteryId,
            "chargeCycles": cycle,
        }
        step = int(step)
        new_soc = soc - uniform((step), (step) * 0.5)
        new_soh = soh - uniform((step), (step) * 0.5)

        soc = new_soc if new_soc > 0 else soc
        soh = new_soh if new_soh > 0 else soh

        predictions.append(prediction)

    return predictions
