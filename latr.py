
import MySQLdb
import hug

import constants
from constants import sql_templates
from Users import create_user
from Users import get_user

cnx = MySQLdb.connect(host="localhost", user="igoinu", passwd="password", db="latr")

###
# User Handlers
###

@hug.get('/user')
def get_all_users():
    cur = cnx.cursor()
    cur.execute(sql_templates["user"]["get_all"].format(users_table=constants.db["users"]))
    rows = cur.fetchall()
    cur.close()
    return rows

@hug.get('/user/{user_id}')
def get_user_handler(user_id):
    cur = cnx.cursor()
    cur.execute(sql_templates["get_user"].format(user_id=user_id, users_table=constants.db["users"]))
    row=cur.fetchone()
    cur.close()
    return row


@hug.post('/user')
def create_user_handler(username):
    cur = cnx.cursor()
    try:
        cur.execute(sql_templates["create_user"].format(username=username, users_table=constants.db["users"]))
        cnx.commit()
    except MySQLdb.Error as e:
        return "Username may already exist"

    cur.execute(sql_templates["get_username"].format(username=username, users_table=constants.db["users"]))
    row = cur.fetchone()
    cur.close()
    return row

@hug.delete('/user/{user_id}')
def delete_user_handler(user_id):
    cur = cnx.cursor()
    cur.execute(sql_templates["delete_user"].format(user_id=user_id, users_table=constants.db["users"]))
    cnx.commit()
    cur.close()
    return "Operation successful"

###
# Game Handlers
###
@hug.post('/game')
def create_game_handler(game_width, game_height, user_id):
    """ Create a new game """
    # Eventually, do some kind of matchmaking here.
    # For now, just return 1

@hug.get('/game')
def get_games_handler(user_id):
    """ Return the id's of all games a player is a participant in """
    cur = cnx.cursor()
    cur.execute(sql_templates["get_games"].format(user_id=user_id, users_table=constants.db["users"]))
    row = cur.fetchall()
    cur.close()
    return row
