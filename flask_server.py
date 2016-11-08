from flask import Flask, render_template, abort, jsonify, make_response


app = Flask(__name__)

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

@app.route('/api/v1.0/lumberjacks', methods=['GET'])
def get_lumberjacks():
	return jsonify({'lumberjacks': lumberjacks})

@app.route('/api/v1.0/lumberjacks/<int:lj_id>', methods=['GET'])
def get_lumberjack(lj_id):
	lumberjack = list(filter(lambda t: t['id'] == lj_id, lumberjacks))
	if len(lumberjack) == 0:
		abort(404)
	return jsonify({'lumberjack': lumberjack[0]})


if __name__ == '__main__':
	app.run(debug=True)
