import jwt
import os
import time
from config import *

SECRET_KEY = os.environ.get("JWT_SECRET")

EXPIRATION_SECONDS = 7200 #token valide 2 heures

def generate_jwt(pseudo, roles):
    expiration = int(time.time()) + EXPIRATION_SECONDS

    payload = {
        "pseudo": pseudo,
        "roles": roles,
        "exp": expiration
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def decode_jwt(token):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        # mise a jour derniere activite
        user = Utilisateur.query.filter_by(pseudo=data["pseudo"]).first()
        user.derAct = int(time.time())
        db.session.commit()

        return data  # dict contenant pseudo, roles, exp
    except ExpiredSignatureError:
        return {"error": "Token expiré"}
    except InvalidTokenError:
        return {"error": "Token invalide"}