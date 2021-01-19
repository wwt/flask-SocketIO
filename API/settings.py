from flask import Flask
from flask_cors import CORS


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/soods/Google Drive/Course Related/Pluralsight/Python Flask-React/API/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
