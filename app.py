from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for all domains temporarily. Adjust for production.

@app.route('/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello m Python!"})

if __name__ == '__main__':
    app.run(debug=True)
