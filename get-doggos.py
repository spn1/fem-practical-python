import requests

api_url = 'http://shibe.online/api'
animals = ['shibes', 'birds', 'cats']
params = {
   "count": 10,
   'https': 'true'
}

response = requests.get(f'{api_url}/birds', params=params)

print(f'Status: {response.status_code}')

data = response.json()

print(data);