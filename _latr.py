
import MySQLdb
import hug

import constants
from constants import sql_templates
import falcon

from Resources import Game, User
from db import cnx

# /user
# POST /user?<username> Create user
# GET  /user/{user_id} Get a given user object
# POST /user/{user_id}/{game_id} Join a game
# DEL  /user/{user_id}/{game_id} Leave a game
#
# GET /game/{game_id} Get / poll a game
# POST /game/{game_id}?<move> Make a move. Maybe hold body in req body?

@hug.post('/user')
def create_user(username):
    """ create a new user """
    username = username.lower()
    user = User()
    user.create({"username":username})
    return user.read()

@hug.get('/user')
@hug.get('/user/{iden}')
def get_user(iden):
    return User(iden).read()


@hug.post('/home')
def post_method():
    return "you used a post method!"
