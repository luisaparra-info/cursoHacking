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


resp = requests.get('http://ip-api.com/json/88.26.236.2')
data= json.loads(resp.content)
print(data["status"])
print(data["city"])