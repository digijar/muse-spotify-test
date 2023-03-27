from flask import Flask, jsonify

app = Flask(name)

@app.route('/api/data')
def get_data():
    data = {"name": "John", "age": 30}
    return jsonify(data)