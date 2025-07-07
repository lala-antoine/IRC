import jwt
import datetime
from flasgger import Swagger
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import db, User
from utils.jwt_utils import generate_jwt
import os

JWT_SECRET = os.environ.get("JWT_SECRET")

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    pseudo = data.get("pseudo")
    password = data.get("password")
    
    if not pseudo or not password:
        return jsonify({"error" : "pseudo ou password manquant"}), 400

    user = User.query.filter_by(pseudo=pseudo).first()
    
    if not user:
        return jsonify({"error" : "utilisateur inconnu"}), 404
    
    if not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Mot de passe incorrect"}), 401
    
    roles = User.query("roles").filter_by(pseudo=pseudo).first()
    
    token = generate_jwt(user.pseudo, roles)
    
    return jsonify({"token" : token}), 200