
import MySQLdb
import hug

import constants
from Users import create_user
from Users import get_user

db = MySQLdb.connect(host="localhost", user="igoinu", passwd="password", db="latr")

cur = db.cursor()


@hug.get('/user/{userid}')
def get_user_handler(userid):
    cur = db.cursor()
    cur.execute(get_user(userid))
    row=cur.fetchone()
    return row
