from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
  return render_template('hello.html', name=name)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')


@app.route('/about')
def about():
  return render_template('about.html')


#error handler methods
@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 404


if __name__ == '__main__':
  app.run()
