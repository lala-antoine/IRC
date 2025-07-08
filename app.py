from config import *
from utils.jwt_utils import generate_jwt, decode_jwt

EXEMPT_ROUTES = ['/login', '/register', '/']

@app.before_request
def check_jwt_globally():
    if request.path in EXEMPT_ROUTES:
        return  # on laisse passer sans vérifier le JWT

    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Token manquant"}), 401

    token = auth_header.split(" ")[1]
    payload = decode_jwt(token)

    if "error" in payload:
        return jsonify(payload), 401

@app.route("/register", methods=["POST"])
def register():
    """Crée un nouvel utilisateur.
    Requête JSON attendue :
    {
        "pseudo": "string",
        "email": "string",
        "password": "string",
        "avatar": "string (url)"  # optionnel
    }
    """

    data = request.get_json(silent=True) or {}
    required = {"pseudo", "email", "password"}

    # Validation du json
    if not required.issubset(data):
        return jsonify(error="Champs obligatoires: pseudo, email, password"), 400

    # Cas utilisateur déja existant
    if Utilisateur.query.get(data["pseudo"]) or Utilisateur.query.filter_by(email=data["email"]).first():
        return jsonify(error="Pseudo ou email déjà utilisé"), 409

    # Création de l'utilisateur
    utilisateur = Utilisateur(
        pseudo=data["pseudo"],
        email=data["email"],
        password=generate_password_hash(data["password"]),
        avatar=data.get("avatar"),
        derAct=int(time.time()),
        statut="actif",
    )

    # Attribution du rôle "user" par défaut
    role_user = Role.query.get("user")
    utilisateur.roles.append(role_user)

    db.session.add(utilisateur)
    db.session.commit()

    return (
        jsonify(
            {
                "pseudo": utilisateur.pseudo,
                "email": utilisateur.email,
                "statut": utilisateur.statut,
                "roles": [r.nom for r in utilisateur.roles],
                "avatar": utilisateur.avatar,
            }
        ),
        201,
    )


@app.route("/whois/<pseudo>", methods=["GET"])
def whois(pseudo):
    utilisateur = Utilisateur.query.get(pseudo)
    if not utilisateur:
        return (
            jsonify(error="Utilisateur inconnu"),
            404
        )

    return (
        jsonify(
            {
                "pseudo": utilisateur.pseudo,
                "cannaux": ["TODO"], # TODO voir pour les cannaux
                "statut": utilisateur.statut,
                "derAct": utilisateur.derAct,
                "roles": [r.nom for r in utilisateur.roles],
            }
        ),
        200
    )

@app.route('/login', methods=['POST'])
def login():
    
    """   
    Description
    ---
    parameters:
      - name: login
        in: body
        required: true
        schema:
          type: object
          properties:
            pseudo:
              type: string
              example: "Roger"
            password:
              type: string
              example: "CoinCoin"
    responses:
      200:
        description: "Ok"
      401:
        description: "Mot de passe incorrect"
      404:
        description: "Utilisateur Inconnu"
    """
    
    data = request.get_json()
    pseudo = data.get("pseudo")
    password = data.get("password")
    
    if not pseudo or not password:
        return jsonify({"error" : "pseudo ou password manquant"}), 400

    user = Utilisateur.query.filter_by(pseudo=pseudo).first()
    
    if not user:
        return jsonify({"error" : "utilisateur inconnu"}), 404
    
    if not check_password_hash(user.password, password):
        return jsonify({"error": "Mot de passe incorrect"}), 401
    
    roles = [r.nom for r in user.roles]

    token = generate_jwt(user.pseudo, roles)
    
    return jsonify({"token" : token}), 200



@app.route("/seen/<pseudo>", methods=["GET"])
def seen(pseudo):
    utilisateur = Utilisateur.query.get(pseudo)

    if not utilisateur:
        return (
            jsonify(error="Utilisateur inconnu"),
            404
        )

    return jsonify(
        {
            "pseudo": utilisateur.pseudo,
            "derAct": utilisateur.derAct,
        }
    )

@app.route("/user/<pseudo>/password", methods=["PATCH"])
def change_password(pseudo):

    auth_header = request.headers.get('Authorization')
    token = auth_header.split(" ")[1]
    data = decode_jwt(token)

    if pseudo != data["pseudo"]:
        return jsonify(error="l'utilisateur connecté n'est pas le même que celui en argument"), 400

    data = request.get_json()
    old_password = data.get("old_password")
    new_password = data.get("new_password")

    if not pseudo or not old_password or not new_password:
        return jsonify({"error" : "pseudo, old_password ou new_password manquant"}), 400

    user = Utilisateur.query.filter_by(pseudo=pseudo).first()
    
    if not user:
        return jsonify({"error" : "utilisateur inconnu"}), 404
    
    if not check_password_hash(user.password, old_password):
        return jsonify({"error": "ancien mot de passe incorrect"}), 401

    user.password = generate_password_hash(new_password)

    db.session.commit()

    return jsonify({"message": "Mot de passe mis à jour avec succès"}) , 200


@app.route("/user/status", methods=["POST"])
def change_status():
    """"
    Value possible : "actif", "inactif", "banni"
    """
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Token manquant"}), 401

    token = auth_header.split(" ")[1]
    data = decode_jwt(token)
    json = request.get_json()
    utilisateur = Utilisateur.query.get(data["pseudo"])
    try:
        utilisateur.statut = json["statut"]
        db.session.commit()
    except ValueError:
        return jsonify({"error": "Statut invalide (Valeur possible : \"actif\", \"inactif\", \"banni\")"}), 400

    return jsonify({"result": "OK"}), 200

@app.route("/user/avatar/<pseudo>", methods=["GET"])
def get_avatar(pseudo):
    utilisateur = Utilisateur.query.get(pseudo)

    if not utilisateur:
        return (
            jsonify(error="Utilisateur inconnu"),
            404
        )

    return jsonify({"avatar": utilisateur.avatar}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5001")))


