import requests

response = requests.get('http://172.17.0.2:5000/ping')

print('the time for app1 is', response.json()['time'])