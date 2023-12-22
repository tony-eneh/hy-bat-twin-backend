import json
from datetime import datetime
from flask import request


def response(data, message="Successful"):
    return {
        "success": True,
        "message": message,
        "data": data,
    }


ba3s = [
    {
        "id": 1,
        "name": 'Battery 1',
        "dataSource": 'XXXXXXXXXXXXXXXXXXXX',
        "createdAt": "2023-12-01",
        'description': 'This battery is used for everything nice',
        "image": '/images/battery.png',
        "chargeCycles": 5
    },

    {
        "id": 2,
        "name": 'Battery 2',
        "dataSource": '',
        "createdAt": "2023-12-02",
        'description': 'Used in my private car',
        "image": '/images/battery.png',
        "chargeCycles": 15
    },
    {
        "id": 3,
        "name": 'Battery 3',
        "dataSource": 'XXXXXXXXXXXXXXXXXXXX',
        "createdAt": "2023-12-03",
        'description': 'Official vehicle battery, zSdZ2ZsHEYx59 UvJk/GxP/5H/I E/4C/8 kzwa/rVss EaI5PgM9 MeFzZ22c XrV9q 4t2kvP6Amhl iaf4fjo L/Qn+pv8g/xL6aT+ fdb4D/4ef/zVa1u 3Sj5N BQmTuCWE 3Kk8yg39 ERluWKn ZbybJbtnmj3K/2s8SJF8l8QF0XBc w3GAn9UG z 6p 28V21 MMjsPyPixhQ3 Vp zK3G7A/ Official vehicle battery, zSdZ2ZsHEYx59 UvJk/GxP/5H/I E/4C/8 kzwa/rVss EaI5PgM9 MeFzZ22c XrV9q 4t2kvP6Amhl iaf4fjo L/Qn+pv8g/xL6aT+ fdb4D/4ef/zVa1u 3Sj5N BQmTuCWE 3Kk8yg39 ERluWKn ZbybJbtnmj3K/2s8SJF8l8QF0XBc w3GAn9UG z 6p 28V21 MMjsPyPixhQ3 Vp zK3G7A/ Official vehicle battery, zSdZ2ZsHEYx59 UvJk/GxP/5H/I E/4C/8 kzwa/rVss EaI5PgM9 MeFzZ22c XrV9q 4t2kvP6Amhl iaf4fjo L/Qn+pv8g/xL6aT+ fdb4D/4ef/zVa1u 3Sj5N BQmTuCWE 3Kk8yg39 ERluWKn ZbybJbtnmj3K/2s8SJF8l8QF0XBc w3GAn9UG z 6p 28V21 MMjsPyPixhQ3 Vp zK3G7A/ Official vehicle battery, zSdZ2ZsHEYx59 UvJk/GxP/5H/I E/4C/8 kzwa/rVss EaI5PgM9 MeFzZ22c XrV9q 4t2kvP6Amhl iaf4fjo L/Qn+pv8g/xL6aT+ fdb4D/4ef/zVa1u 3Sj5N BQmTuCWE 3Kk8yg39 ERluWKn ZbybJbtnmj3K/2s8SJF8l8QF0XBc w3GAn9UG z 6p 28V21 MMjsPyPixhQ3 Vp zK3G7A/',
        "image": '/images/battery.png',
        "chargeCycles": 234
    },
]

dataSources = [
    {
        "id": 1,
        "name": "Car Battery For Lab",
        "createdAt": datetime.now().isoformat(),
        # readings: []
    },
    {
        "id": 2,
        "name": "Inverter battery",
        "createdAt": datetime.now().isoformat(),
        # readings: []
    },
    {
        "id": 3,
        "name": "Car backup ba3",
        "createdAt": datetime.now().isoformat(),
        # readings: []
    },
]


def find(condition, iterable):
    for element in iterable:
        if condition(element):
            return element
    return None


def preprend_host_url_to_images(ba3s):
    for ba3 in ba3s:
        if (ba3['image'].startswith('/')):
            ba3['image'] = request.root_url + ba3['image'][1:]

    return ba3s
