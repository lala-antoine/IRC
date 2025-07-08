from flasgger import Swagger
from flask import Flask


app = Flask(__name__)
swagger = Swagger(app)

@app.route("/login", methods=["POST"])
def post_login():
    
    """
    Connecte l'utilisateur et renvoie un jeton JWT
---
produces:
  - application/json
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
    description: "Connexion réussie, JWT retourné"
    schema:
      type: object
      properties:
        token:
          type: string
          example: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
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
            statut:
              type: string
              example: "actif"
            roles:
              type: array
              items:
                types: string
                example: ["user","..."]
      400:
        description: "Champs obligatoires manquants"
      409:
        description: "Pseudo ou email déjà utilisé"
      404:
        description: "Utilisateur Inconnu"
    """
    
    return "Retourne rien"


@app.route("/whois/<pseudo>", methods=["GET"])
def get_whois(pseudo):
    
    """
    Récupère les informations de l'utilisateur connecté
---
parameters:
  - name: pseudo
    in: path
    type: string
    required: true
    description: pseudo
    example : Quack Sparrow
responses:
  200:
    description: "Utilisateur trouvé"
    schema:
      type: object
      properties:
        pseudo:
          type: string
          example: "Roger"
        cannaux:
          type: array
          items:
            type: string
          example: ["TODO"]
        statut:
          type: string
          example: "en ligne"
        derAct:
          type: int
          example: "11215568894543"
        roles:
          type: array
          items:
            type: string
          example: ["admin", "moderateur"]
  404:
    description: "Utilisateur inconnu"
    schema:
      type: object
      properties:
        error:
          type: string
          example: "Utilisateur inconnu"

    """
    
    return "Retourne rien"

app.run()