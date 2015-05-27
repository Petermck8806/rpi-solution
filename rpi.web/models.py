__author__ = 'pmckinney'

from datetime import datetime

from __init__ import db

class Image(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  image = db.Column(db.BLOB, nullable=True)
  type = db.Column(db.Text, nullable=False)
  filename = db.Column(db.Text, nullable=False)


  def __repr__(self):
    return "<Image '{}': '{}'>".format(self.filename,self.type)
