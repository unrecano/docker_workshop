import os
import uuid
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(80), nullable=False)

    def __init__(self, first_name, last_name, country):
    	self.first_name = first_name
    	self.last_name = last_name
    	self.country = country

def response_user(resource):
	if isinstance(resource, list):
		response = []
		for user in resource:
			element = {
				'id': user.id,
				'first_name': user.first_name,
				'last_name': user.last_name,
				'country': user.country
			}
			response.append(element)
	else:
		response = {
			'id': resource.id,
			'first_name': resource.first_name,
			'last_name': resource.last_name,
			'country': resource.country
		}
	return response

@app.route('/')
def index():
	return 'Hello World!'

# CREATE new user.
@app.route('/users', methods=['POST'])
def create_users():
	print(request.json)
	user = User(
		first_name=request.json['first_name'],
		last_name=request.json['last_name'],
		country=request.json['country'])
	db.session.add(user)
	db.session.commit()
	return jsonify(response_user(user)), 201

# READ all users.
@app.route('/users')
def get_users():
	users = User.query.all()
	return jsonify(response_user(users))

# READ an user.
@app.route('/users/<string:id>')
def get_user(id):
	user = User.query.get(id)
	return jsonify(response_user(user))

# UPDATE an user.
@app.route('/users/<string:id>', methods=['PUT', 'PATCH'])
def update_user(id):
	user = User.query.get(id)
	data = request.json
	user.first_name = data['first_name'] if 'first_name' in data else user.first_name
	user.last_name = data['last_name'] if 'last_name' in data else user.last_name
	user.country = data['country'] if 'country' in data else user.country
	db.session.add(user)
	db.session.commit()
	return jsonify(response_user(user))

# DELETE an user.
@app.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
	user = User.query.get(id)
	db.session.delete(user)
	db.session.commit()
	return jsonify({}), 204

if __name__ == '__main__':
	db.create_all()
	app.run(host='0.0.0.0', port=8002, debug=True)