from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/random', methods=['GET'])
def get_random_number():
    return jsonify({"random_number": random.randint(1, 100)})

if __name__ == '__main__':
    app.run(debug=True)
