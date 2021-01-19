from flask import Flask
from flask_cors import CORS
import pathlib

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(pathlib.Path().absolute()) + '/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
