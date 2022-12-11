import json
from flask import Flask, jsonify, request
app = Flask(__name__)
data = [{'id': 0, 'name': 'Alex', 'surname': 'Turner'},
        {'id': 1, 'name': 'Thom', 'surname': 'Yorke'}]


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data)


@app.route('/users', methods=['POST'])
def add_user():
    #print(request.get_json()['name'])
    data.append({'name': 'Roma'})
    return jsonify(data)


@app.route('/users', methods=['DELETE'])
def del_user():
    data.remove({'name': 'Roma'})
    return jsonify(data)

# не смог разобраться как делать этот метод PUT
@app.route('/users', methods=['PUT'])
def update_user():
    data.put({'name': 'Alex'})
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
