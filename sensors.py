from random import randrange
from datetime import datetime


def getReadings(id):
    readings = []

    for i in range(33):
        reading = {
            "temperature": randrange(1, 83),
            "voltage": randrange(5, 12),
            "current": randrange(1, 100),
            "createdAt": datetime.now().isoformat(),
            "batteryId": id,
        }

        readings.append(reading)

    return readings
