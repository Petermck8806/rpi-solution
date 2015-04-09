import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


#configuration
app.config['DATABASE_URI'] = 'RPIImages.db'
app.config['DEBUG'] = True

db = SQLAlchemy(app)

if __name__ == '__main__':
  app.run()


import models
import views
