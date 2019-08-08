from flask import Flask
from flask_restful import Api
from coke_logo_detection.resources.coke import Coke

app = Flask(__name__)

api = Api(app)

api.add_resource(Coke, '/coke-logo-detection/api/image')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
