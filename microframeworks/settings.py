from datetime import datetime 
HOST = '0.0.0.0'
PORT = 8000

JSON_DATA = {
    'test': True,
    'date': datetime.now(),
    'values' : [1,2,3,4,5],
    'sub_attributes': {
        'attribute1': 1,
        'attribute2' : 'True',
    }
}

TEXT = 'Hello World!'