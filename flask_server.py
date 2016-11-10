from flask import Flask, render_template, abort, jsonify, make_response, request
from database import create_user, get_all_users
from lj_models import User


app = Flask(__name__)
api_path = '/api/v1.0/'


lumberjacks = [
	{
		'id':1,
		'name':'Browsing the deep web',
		'start': '07.11.2016 21:43',
		'end':'07.11.2015 22:15'
	},
	{
		'id':2,
		'name':'Doing some productive work',
		'start':'07.11.2016 22:15',
		'end':''
	}
]

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'Not Found'}), 404)


@app.route('/')
def home_page():
	return render_template('index.html')


@app.route(api_path + 'lumberjacks', methods=['GET'])
def get_lumberjacks():
	return jsonify({'lumberjacks': lumberjacks})


@app.route(api_path + 'users/', methods=['POST'])
def new_user():
	if not request.json or not 'email' in request.json:
		abort(400)
	user = {'name': request.json['name'], 'email': request.json['email'], 'password': request.json['password'] }
	user = User(request.json['name'], request.json['email'], request.json['password'])
	create_user(user)


@app.route(api_path + 'users/', methods=['GET'])
def get_users():
	result = get_all_users()
	return jsonify({'users': result})


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
