from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import basedir
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
