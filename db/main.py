# client side
# author Sitdikov R.A.
# group M30-312B-20

from flask import Flask, jsonify, request, render_template
#from flask_restful import Api, Resource, reqparse # импортируем классы
import psycopg2

app: Flask = Flask(__name__) # создаем приложение, передаем название файла __name__
#api = Api() # создаем объект на основе класса API для взаимодействия с REST
data = []
error = [{"information":96,"text":"Invalid user ID. ",
               "result":"Make sure you are using the correct ID."}]

conn = psycopg2.connect(
    host="localhost",
    database="my_db",
    user="roma",
    password="12345"
)

cursor = conn.cursor()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/users', methods=['GET'])
def get_users():
    data.clear()
    sql = 'SELECT * FROM users;'
    cursor.execute(sql)
    base = cursor.fetchall()
    conn.commit()
    print(base)
    for i in base:
        user = {'id': i[0], 'name': i[1], 'surname': i[2]}
        data.append(user)
    print(data)
    return jsonify(data)
  
@app.route('/users', methods=['PUT'])
def update_user():
    get_users()
    for i in data:
        if request.get_json()['id'] == i['id']:
            sql = "UPDATE users SET id = %s, name =%s, lastname =%s WHERE id = %s;"
            id = request.get_json()['id']
            name = request.get_json()['name']
            lastname = request.get_json()['lastname']
            cursor.execute(sql, (id, name, lastname, id))
            conn.commit()
            return jsonify(data)
    return jsonify(error)

@app.route('/users', methods=['DELETE'])
def del_user():
    get_users()
    for i in data:
        if request.get_json()['id'] == i['id']:
            command = 'DELETE FROM users WHERE id=%s;'
            id = request.get_json()['id']
            cursor.execute(command, (id,))
            conn.commit()
            return jsonify(data)
    return jsonify(error)

@app.route('/users', methods=['POST'])
def add_user():
    command = 'INSERT INTO users VALUES (default, %s, %s);'
    name = request.get_json()['name']
    lastname = request.get_json()['surname']
    cursor.execute(command, (name, lastname))
    conn.commit()
    return jsonify(data)



# book = {
#     1: {"name": "vasya", "age": 15},
#     2: {"name": "sasha", "age": 33}
# }
#
# parser = reqparse.RequestParser()
# parser.add_argument("name", type=str)
# parser.add_argument("type", type=int)
#
# # основной класс с наследованием
# # от reqparse для возможности обработки GET/PUT/DEL запросов
# class Main(Resource):
#     def get(self, book_id):
#         if book_id == 0:
#             return book
#         else:
#             return book[book_id]
#
#     def delete(self, book_id):
#         del book[book_id]
#         return book
#
#     def post(self, book_id):
#         book[book_id] = parser.parse_args()
#         return book
#
#     def put(self, book_id):
#         book[book_id] = parser.parse_args()
#         return book
#
#
# api.add_resource(Main, "/api/book/<int:book_id>") # добавляем в обработку url адреса
# api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="127.0.0.1") # запуск проекта проверка - вывод ошибок в консоль,
