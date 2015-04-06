import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, send_from_directory
from contextlib import closing


#configuration
DATABASE = 'RPIImages.db'
DEBUG = True


#create application
app = Flask(__name__)
app.config.from_object(__name__)

#database methods
def connect_db():
  return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_request():
  g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
  db = getattr(g, 'db', None)
  if db is not None:
    db.close()


#error handler methods
@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 404


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/settings')
def settings():
  return render_template('settings.html')


@app.route('/view_image/<path:filename>')
def view_image(filename):
  return send_from_directory('/static/img',filename)


@app.route('/display_image')
def display_image():
  return render_template('displayimage.html');


if __name__ == '__main__':
  app.run()
