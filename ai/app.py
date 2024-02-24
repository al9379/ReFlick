from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

@app.route('/api/data')
def get_data():
    return jsonify({'data': 'Hello from Flask!'})

if __name__ == '__main__':
    app.run(debug=True)