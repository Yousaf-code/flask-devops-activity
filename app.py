# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True)
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)
