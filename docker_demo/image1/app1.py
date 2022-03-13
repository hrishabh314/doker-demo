from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping')
def ping():
	from datetime import datetime

	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")
	
	res = {
		'status' : True,
		'time' : current_time
	}

	return jsonify(res)

if __name__ == '__main__':
	app.run(host = '0.0.0.0')
