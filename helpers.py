import json
from datetime import datetime


def response(data):
    return {
        "success": True,
        "message": "Successful",
        "data": data,
    }


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
