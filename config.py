import os
import time

import sqlalchemy
from flasgger import Swagger, swag_from
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash

from models import Utilisateur, Role, db

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
swagger = Swagger(app)

# Création des tables si nécessaire
for i in range(10):
    try:
        with app.app_context():
            db.create_all()
            """Crée les rôles de base ('user', 'admin') s'ils n'existent pas."""
            for role_name in ("user", "admin"):
                if not Role.query.get(role_name):
                    db.session.add(Role(nom=role_name))
            db.session.commit()
        break                  # 👍 connexion OK
    except sqlalchemy.exc.OperationalError as e:
        print("DB pas prête, retry dans 3 s…", e)
        time.sleep(3)
else:
    raise RuntimeError("MySQL indisponible après plusieurs tentatives")