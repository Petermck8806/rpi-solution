from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
  return render_template('hello.html', name=name)

@app.route('/')
def index():
  return 'Welcome'

if __name__ == '__main__':
  app.run()