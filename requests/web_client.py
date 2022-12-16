import requests

r = requests.get('http://127.0.0.1:5000/users')
print(r.json())

r = requests.post('http://127.0.0.1:5000/users', json={"name": "Roma", "surname": "Sitdikov"})
print(r.json())

r = requests.put('http://127.0.0.1:5000/users', json={"id": "1", "name": "Peter", "surname": "Ivanov"})
print(r.json())

r = requests.delete('http://127.0.0.1:5000/users', json={"id": "0"})
print(r.json())
