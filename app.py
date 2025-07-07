from config import *

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


@app.route('/login', methods=['POST'])
def login():
    
    """Connecte un utilisateur.
    Requête JSON attendue :
    {
        "pseudo": "string",
        "password": "string",
    }
    """
    
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5001")))


