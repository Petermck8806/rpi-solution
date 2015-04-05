__author__ = 'pmckinney'

import sqlite3
import os.path
from os import listdir, getcwd


def get_image_list(rel_path):
  abs_path = os.path.join(os.getcwd(),rel_path)
  print('abs_path =', abs_path)
  dir_files = os.listdir(abs_path)
  return dir_files

def open_db(db_file):
  if not os.path.exists(db_file):
    return
  conn = sqlite3.connect(db_file)
  return conn

def insert_image(conn, image):
  with open(image, 'rb') as input_file:
    image_blob = input_file.read()
    base = os.path.basename(image)
    afile, ext = os.path.splitext(base)
    sql = '''INSERT INTO IMAGES
    (IMAGE,TYPE,FILENAME)
    VALUES(?, ?, ?);'''
    conn.execute(sql,[sqlite3.Binary(image_blob),ext,afile])
    conn.commit()


def extract_image(cursor, image_id):
    sql = "SELECT image, TYPE, FILENAME FROM images WHERE id = :id"
    param = {'id': image_id}
    cursor.execute(sql, param)
    ablob, ext, afile = cursor.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename

image_list = get_image_list('.\images')
print(image_list)
conn = open_db('..\db\RPIImages.db')
conn.execute("DELETE FROM images")
for fn in image_list:
    image_file = "./images/"+fn
    insert_image(conn, image_file)

for r in conn.execute("SELECT FILENAME FROM images"):
    print(r[0])

conn.close()
