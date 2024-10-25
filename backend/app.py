from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# A simple route that returns a JSON response
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'id': 1,
        'name': 'Dummy Item',
        'description': 'This is a dummy item from the API.'
    }
    return jsonify(data)

# A route to simulate posting data to the server
@app.route('/api/data', methods=['POST'])
def post_data():
    # For demonstration, we'll just return the data received in the request
    request_data = request.json
    return jsonify({
        'message': 'Data received successfully.',
        'receivedData': request_data
    }), 201

@app.route('/api/info')
def info():
	resp = {
		'connecting_ip': request.headers.get['X-Real-IP'],
		'proxy_ip': request.headers['X-Forwarded-For'],
		'host': request.headers['Host'],
		'user-agent': request.headers['User-Agent']
	}

	return jsonify(resp)

if __name__ == '__main__':
    app.run(debug=True)
