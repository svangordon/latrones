
import MySQLdb
import hug

import constants
from constants import sql_templates
import falcon

from game_logic import make_move

from game_class import GameState

cnx = MySQLdb.connect(host="localhost", user="igoinu", passwd="password", db="latr")

###
# User Handlers
###

@hug.get('/user')
def get_all_users():
    """ Returns all users. """
    cur = cnx.cursor()
    cur.execute(sql_templates["user"]["get_all"].format(users_table=constants.db["users"]))
    rows = cur.fetchall()
    cur.close()
    return rows

@hug.get('/user/{user_id}', output=hug.output_format.json)
def get_user(user_id, response=None):
    """ Returns a single user by id. """
    cur = cnx.cursor()
    cur.execute(sql_templates["get_user"].format(user_id=user_id, users_table=constants.db["users"]))
    row=cur.fetchone()
    cur.close()
    if row == None:
        response.status = falcon.HTTP_404
        return "user not found"
    return {'user_id': row[0], 'username': row[1]}


@hug.post('/user', output=hug.output_format.json)
def create_user_handler(username, response=None):
    cur = cnx.cursor()
    try:
        cur.execute(sql_templates["create_user"].format(username=username, users_table=constants.db["users"]))
        cnx.commit()
    except MySQLdb.Error as e:
        response.status = falcon.HTTP_403
        return "Could not add username. {0}".format(e)
    cur.execute(sql_templates["get_username"].format(username=username, users_table=constants.db["users"]))
    row = cur.fetchone()
    cur.close()
    return {'user_id': row[0], 'username': row[1]}

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
# Participant Handlers
###
@hug.local()
@hug.post('/game/{game_id}/{user_id}')
def add_participant(user_id: hug.types.number, game_id: hug.types.number):
    """ Creates a participant and returns the participant id """
    # ??? does this having a side-effect make it overloaded?
    cur = cnx.cursor()
    cur.execute(sql_templates["participant"]["create_participant"].format(user_id=user_id, game_id=game_id, participant_table=constants.db["participant"]))
    cur.execute(sql_templates["util"]["last_insert"])
    cnx.commit()
    row = cur.fetchone()[0]
    cur.close()
    return row

@hug.local()
def get_participant(participant_id: hug.types.number):
    """ Returns a participant dict """
    cur = cnx.cursor()
    cur.execute(sql_templates["participant"]["get_participant"].format(participant_id=participant_id, participant_table=constants.db["participant"]))
    row = cur.fetchone()
    if row == None:
        return None
    cur.close()
    return dict(zip(('participant_id', 'user_id', 'game_id'), row))

@hug.local()
def delete_participant(participant_id: hug.types.number):
    cur = cnx.cursor()
    cur.execute(sql_templates["participant"]["delete_participant"].format(participant_id=participant_id, participant_table=constants.db["participant"]))
    # row = cur.fetchone()
    cur.close()
    return 'deleted'

@hug.local()
def get_participant_by_user(user_id):
    cur = cnx.cursor()
    cur.execute(sql_templates["participant"]["get_participant_by_user"].format(user_id=user_id, participant_table=constants.db["participant"]))
    resp = cur.fetchall()
    cur.close()
    return resp
###
# Local Game Handlers
###
# Not used?
# @hug.local()
# def add_game(user_id, board_width=8, board_height=8):
#     """ Insert a new game row, and return its id """
#     cur = cnx.cursor()
#     cur.execute(sql_templates["game"]["create_game"].format(user_id=user_id, board_width=board_width, board_height=board_height, game_table=constants.db["game"]))
#     cnx.commit()
#     added = get_last_insert(cur)
#     return added

@hug.local()
@hug.delete('/game/{game_id}')
def delete_game(game_id):
    cur = cnx.cursor()
    cur.execute(sql_templates["game"]["delete_game"].format(game_id=game_id, game_table=constants.db["game"]))
    return True

###
# External Game Handlers
###
@hug.post('/game/{user_id}', output=hug.output_format.json)
def create_game_handler(user_id, game_type="standard", game_options=None, response=None):
    """ Create a new game """
    if game_options == None:
        game_options = {
            "color": None
        }
    cur = cnx.cursor()
    game = GameState("standard", True)
    cur.execute(sql_templates["game"]["create_game"].format(start_fen=game.fen_string, color=game_options.color, user_id=user_id.db["game"]))
    game_id = cur.fetchone()
    # cur.execute(sql_templates["util"]["last_insert"])
    # game_id = cur.fetchone()[0]
    # game_id = add_game(user_id, board_width, board_height)
    # participant_id = add_participant(user_id, game_id)
    # cur.execute(sql_templates["participant"]["create_participant"].format(user_id=user_id, game_id=game_id, participant_table=constants.db["participant"]))
    # cur.execute(sql_templates["util"]["last_insert"])
    # participant_id = cur.fetchone()[0]
    cnx.commit()
    cur.close()
    return get_game(game_id)
    # return {"game_id": game_id, "participant_id": participant_id}

@hug.local()
@hug.get('/game/{game_id}')
def get_game(game_id, response=None):
    cur = cnx.cursor()
    cur.execute(sql_templates["game"]["get_game"].format(game_id=game_id))
    row = cur.fetchone()
    if row == None:
        if response:
            response.status = falcon.HTTP_404
            return "game not found"
        return None
    return dict(zip(('game_id', 'start_time', 'initial'), row))

# @hug.get('/game/{user_id}')
# def get_games_handler(user_id):
#     """ Return the id's of all games a player is a participant in """
#     cur = cnx.cursor()
#     cur.execute(sql_templates["participant"]["get_participant_games"].format(user_id=user_id, participant_table=constants.db["participant"]))
#     row = cur.fetchall()
#     cur.close()
#     return row

@hug.get('/games')
def get_all_games_handler():
    cur = cnx.cursor()
    cur.execute(sql_templates["game"]["get_all_games"].format(game_table=constants.db["game"]))
    row = cur.fetchall()
    cur.close()
    return row

@hug.get('/games/user/{user_id}')
def get_games_by_user(user_id, response=None):
    cur = cnx.cursor()
    cur.execute(sql_templates["game"]["get_by_user"].format(user_id=user_id))
    row = cur.fetchall()
    cur.close()
    return row

###
# Move Handlers
###
@hug.local()
def get_moves_by_game(game_id):
    cur = cnx.cursor()
    cur.execute(sql_templates["move"]["get_moves"].format(game_id=game_id))
    row=cur.fetchall()
    cur.close()
    return row

@hug.local()
def add_move(move_dict):
    cur = cnx.cursor()
    cur.execute(sql_templates["move"]["add_move"].format(**move_dict))
    cnx.commit()
    row = get_last_insert(cur)
    return row
    # return get_last_insert(cur)

@hug.local()
def delete_move(move_id):
    cur = cnx.cursor()
    cur.execute(sql_templates["move"]["delete_move"].format(move_id=move_id))
    cur.close()
    return "move deleted"

@hug.local()
def get_move(move_id):
    cur = cnx.cursor()
    cur.execute(sql_templates["move"]["get_move"].format(move_id=move_id))
    row = cur.fetchone()
    cur.close()
    return row

@hug.local()
def do_move(game_id, move_string):
    moves = get_moves_by_game(game_id)
    fen_input = moves[-1][-1]
    result = make_move(fen_input, move_string)
    result["game_id"] = game_id
    add_move(result)

###
# Util Handlers
###
@hug.local()
def get_last_insert(cur):
    """ Convenience function for getting the id of the last inserted row and closing cursor"""
    # cur = cnx.cursor()
    cur.execute(sql_templates["util"]["last_insert"])
    row = cur.fetchone()[0]
    cur.close()
    return row
