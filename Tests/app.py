from flasgger import Swagger
from flask import Flask


app = Flask(__name__)
swagger = Swagger(app)

@app.route("/route", methods=["POST"])
def get_route():
    
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

app.run()