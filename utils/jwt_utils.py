import jwt
import os
import time

SECRET_KEY = os.environ.get("JWT_SECRET")

EXPIRATION_SECONDS = 600 #token valide 10 minutes

def generate_jwt(pseudo, roles):
    expiration = int(time.time()) + EXPIRATION_SECONDS

    payload = {
        "pseudo": pseudo,
        "roles": roles,
        "exp": expiration
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token