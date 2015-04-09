# rpi-solution

RPI-Solution is a raspberry pi project that submits images taken by the raspberry PI camera module to a webservice. The images are then displayed on the rpi-web application.

Prerequisuites:

SQL Alchemy: https://pypi.python.org/pypi/SQLAlchemy/1.0.0b5
  - It is probably more convenient to run 'pip install SQLAlchemy'
  - 'pip install Flask-SQLAlchemy'
SQLite: http://www.sqlite.org/download.html
  - Make sure to download both the sqlite-shell and sqlite-dll files. Recommended to install to C:\sqlite folder. Add sqlite to path if using windows.
Flask and Virtualenv: http://flask.readthedocs.org/en/0.3.1/installation/#windows-easy-install
  - Don't forget to add python to your path if you are using windows.
