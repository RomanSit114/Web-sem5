# client side
# author Sitdikov R.A.
# group M30-312B-20

# import requests # библиотека для обращения по url адресу
#
# res = requests.put("http://127.0.0.1:5000/api/book/2", json={"name": "roma", "age": 55}) # response from the server ответ от сервера, обновляем данные на сервере


import requests
#res = requests.get('http://127.0.0.1:5000/users')
#print(r.json())
#res = requests.post('http://127.0.0.1:5000/users', json={'name': "Jerry", 'lastname': "Petrov"})
#print(r.json())
#res = requests.delete('http://127.0.0.1:5000/users', json={'id': 3})

res = requests.put('http://127.0.0.1:5000/users', json={'id': 3, 'name': 'Georg', 'lastname': 'Ivanov' })
print(res.json())
