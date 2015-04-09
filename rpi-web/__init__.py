__author__ = 'pmckinney'

import os

from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.apth.dirname(__file__))

#configuration
app = Flask(__name__)
app.config['DATABASE_URI'] = 'RPIImages.db'
app.config['DEBUG'] = True

import models
import views
