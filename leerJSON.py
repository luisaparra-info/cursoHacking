import json
import requests


with open('data.json') as file:
    data = json.load(file)
    for client in data['clients']:
        print('First name:', client['first_name'])
        print('Last name:', client['last_name'])
        print('Age:', client['age'])
        print('Amount:', client['amount'])
        print('')


resp = requests.get('http://ip-api.com/json/208.80.152.201')
json.loads(resp.content)