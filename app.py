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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5001")))
