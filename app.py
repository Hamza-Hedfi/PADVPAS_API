from flask import Flask
from flask_restful import Api
from resource.classification import Classification
import os

app = Flask(__name__)
api = Api(app)

api.add_resource(Classification, '/classification')

if __name__ == '__main__':
    app.run(debug=True)
