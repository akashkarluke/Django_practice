import requests
base_url = 'http://127.0.0.1:8000/'
endpoint = 'api/json/'
response = requests.get(base_url+endpoint)
print(type(response))
data = response.json()
print(data)