#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "Ivanov Ivan"
    },
    {
        "id": 2,
        "name": "Petrov Petr"
    },
]


@app.route('/', methods=['GET'])
def index():
    return jsonify(dict())


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):

    return jsonify({'user': next(
        filter(lambda x: x['id'] == user_id, users), {})})


@app.route('/user/add', methods=['POST'])
def get_tasks():
    _id = 0
    try:
        data = request.json
        users.append(
            {'id': data['id'], 'name': data['name']}
        )
        _id = data['id']
    finally:
        return jsonify({'result': _id})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
