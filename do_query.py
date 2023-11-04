import json
import requests
url ="http://127.0.0.1:8000"
requests.get(url=url)
# <Response [200]>
headers = {"Content-Type": "application/json", "accept": "application/json"}
r = requests.get(url=url, headers=headers)
r.json()
# {'message': 'hello world'}

url ="http://127.0.0.1:8000/todos"
r = requests.get(url=url, headers=headers)
r.json()
# [{'task': 'task 1', 'is_completed': True, 'id': 1}]

url ="http://127.0.0.1:8000/todos?completed=true"
r = requests.get(url=url, headers=headers)
r.json()
# [{'task': 'task 1', 'is_completed': True, 'id': 1}]

url ="http://127.0.0.1:8000/todos?completed=false"
r = requests.get(url=url, headers=headers)
# <Response [200]>
# r.json()

payload = {"task":"another task","is_completed": False}
url ="http://127.0.0.1:8000/todos"
r = requests.post(url=url, headers=headers, data=json.dumps(payload))
r.json()
# {'task': 'another task'}

requests.get(url=url, headers=headers).json()
# [{'task': 'task 1', 'is_completed': True, 'id': 1}, {'task': 'another task', 'is_completed': False, 'id': 2}]

