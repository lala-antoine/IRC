from flasgger import Swagger
from flask import Flask


app = Flask(__name__)
swagger = Swagger(app)

@app.route("/route", methods=["GET"])
def get_route():
    
    """
    Doc swagger ici
    """
    
    return "Retourne rien"

app.run()