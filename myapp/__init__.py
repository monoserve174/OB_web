from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from myapp.configs import Config

app = Flask("myapp")
app.config.from_object(Config)
db = SQLAlchemy(app)

from myapp.models import *
from myapp.routes import *