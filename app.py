from flasgger import Swagger
from flask import Flask

app = Flask(__name__)
swagger = Swagger(app)