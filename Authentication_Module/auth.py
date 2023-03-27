from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import bcrypt

app = Flask(__name__)
CORS(app)
mongo_uri = "mongodb+srv://esdmuse:esdmuse@musecluster.egcmgf4.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri, ssl=True, tlsAllowInvalidCertificates=True)
db = client.ESD_Muse

@app.route('/api/authenticate', methods=['POST'])
def authenticate_user():
    email = request.json.get('email')
    password = request.json.get('password')

    user = db.user.find_one({'email': email})
    print(user)
    stored_hash = user['password']
    print(type(stored_hash))
    if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        return jsonify({'success': True, 'access_token': email})
    else:
        return jsonify({'success': False})
    
@app.route('/api/createUser', methods=['POST'])
def create_user():
    email = request.json.get('email')
    password = request.json.get('password')
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    try:
        db.user.insert_one({'email': email, 'password': hashed_password})
        return jsonify({'success': True})
    except :
        return jsonify({'success': False})

    


if __name__ == '__main__':
    app.run(debug=True)
