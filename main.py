from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def random_number():
    number = random.randint(1, 100)  # Random number between 1 and 100
    return jsonify({"random_number": number})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
  
