from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data storage
users = []
next_id = 1


# GET /users → Return all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# GET /users/<id> → Return user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


# POST /users → Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_user = {
        "id": next_id,
        "name": data['name'],
        "email": data['email']
    }

    users.append(new_user)
    next_id += 1

    return jsonify(new_user), 201


if __name__ == '__main__':
    app.run(debug=True)
