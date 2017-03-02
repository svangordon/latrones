
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
        return "Could not add username. {0}".format(e)

    cur.execute(sql_templates["get_username"].format(username=username, users_table=constants.db["users"]))
    row = cur.fetchone()
    cur.close()
    return row

@hug.delete('/user/{user_id}')
def delete_user_handler(user_id):
    cur = cnx.cursor()
    try:
        cur.execute(sql_templates["delete_user"].format(user_id=user_id, users_table=constants.db["users"]))
        cnx.commit()
    except MySQLdb.Error as e:
        return "Could not delete user. {0}".format(e[0])
    cur.close()
    return "Operation successful"

###
# Game Handlers
###
@hug.post('/game/create', output=hug.output_format.json)
def create_game_handler(user_id, board_width, board_height):
    """ Create a new game """
    cur = cnx.cursor()
    cur.execute(sql_templates["game"]["create_game"].format(board_width=board_width, board_height=board_height, game_table=constants.db["game"]))
    cur.execute(sql_templates["util"]["last_insert"])
    game_id = cur.fetchone()[0]
    cur.execute(sql_templates["participant"]["create_participant"].format(user_id=user_id, game_id=game_id, participant_table=constants.db["participant"]))
    cnx.commit()
    # row = cur.fetchone()
    cur.close()
    return {"status": "success", "game_id": game_id}

@hug.get('/game/get/{user_id}')
def get_games_handler(user_id):
    """ Return the id's of all games a player is a participant in """
    cur = cnx.cursor()
    cur.execute(sql_templates["participant"]["get_participant_games"].format(user_id=user_id, participant_table=constants.db["participant"]))
    row = cur.fetchall()
    cur.close()
    return row

@hug.get('/games')
def get_all_games_handler():
    cur = cnx.cursor()
    cur.execute(sql_templates["game"]["get_all_games"].format(game_table=constants.db["game"]))
    row = cur.fetchall()
    cur.close()
    return row

@hug.delete('/game/{game_id}')
def delete_game_handler():
    cur = cnx.cursor()
    try:
        cur.execute(sql_templates["delete_game"].format(game_id=game_id, game_table=constants.db["game"]))
    except MySQLdb.Error as e:
        return "Could not delete game. {0}".format(e[0])
    cur.close()
    return "Game deleted"
