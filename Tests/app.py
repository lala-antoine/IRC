from flasgger import Swagger
from flask import Flask


app = Flask(__name__)
swagger = Swagger(app)

@app.route("/login", methods=["POST"])
def post_login():
    
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
    
    return "Retourne rien"

@app.route("/register", methods=["POST"])
def post_register():
    
    """
        Crée un nouvel utilisateur
    ---
    parameters:
      - name: user_info
        in: body
        required: 
          - pseudo
          - email
          - password
        schema:
          type: object
          properties:
            pseudo:
              type: string
              example: "Roger"
            email:
              type: string
              example: "CoinCoin@duckdns.org"
            password:
              type: string
              example: "pa_en!plastik"
            avatar:
              type: string
              example: "super_duper_hot_duck.png"
    responses:
      201:
        description: "Ok"
      400:
        description: "Champs obligatoires manquants"
      409:
        description: "Pseudo ou email déjà utilisé"
      404:
        description: "Utilisateur Inconnu"
    """
    
    return "Retourne rien"


app.run()