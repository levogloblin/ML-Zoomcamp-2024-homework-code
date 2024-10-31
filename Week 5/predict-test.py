import requests
 
url = 'http://localhost:9696/predict'

customer = {"job": "management", "duration": 400, "poutcome": "success"}
 
response = requests.post(url, json=customer).json()
print(response)