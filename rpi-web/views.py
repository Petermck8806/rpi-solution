from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, send_from_directory
from contextlib import closing
from __init__ import app


#error handler methods
@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 404


@app.route('/')
@app.route('/index')
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


