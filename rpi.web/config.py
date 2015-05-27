import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	DEBUG = False


class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'RPIImages.db')


#we will need to add a few more configurations to this file for test and production.

#for now, everything will point to development settings.
config_by_name = dict(
	dev = DevelopmentConfig,
	test = DevelopmentConfig,
	prod = DevelopmentConfig
)