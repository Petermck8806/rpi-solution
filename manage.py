import os

from . import create_app, db

from flask.ext.script import Manager

app = create_app(os.getenv('RPISOLUTION_ENV') or 'dev')
manager = Manager(app)

#migrate = Migrate(app, cb)

#manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
	manager.run()