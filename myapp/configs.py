import os
import sys
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
isWin = sys.platform.startswith("win")
db_prefix = 'sqlite:///'
if not isWin:
    db_prefix += '/'


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY", "KevinDevFromConfig")
    SQLALCHEMY_DATABASE_URI = db_prefix + os.path.join(basedir, 'static/database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
