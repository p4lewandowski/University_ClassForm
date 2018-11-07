import json
import requests

def export_database():

    with open('db_backup', 'w') as file:
        data = requests.get('http://127.0.0.1:8000/dbexport/').json()
        file.write(json.dumps(data))


def import_database():

    with open('db_backup', 'r') as file:

        data = requests.post('http://127.0.0.1:8000/dbexport/').json()


export_database()
import_database()