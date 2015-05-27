import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.moment import Moment

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


#configuration
app.config['DATABASE_URI'] = 'RPIImages.db'
app.config['DEBUG'] = True

db = SQLAlchemy(app)

#flask debug toolbar
toolbar = DebugToolbarExtension

#for displaying timestamps
moment = Moment()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config_by_name[config_name])
	db.init_app(app)
	#moment.init_app(app)
	return app


if __name__ == '__main__':
  app.run()


import models
import views
