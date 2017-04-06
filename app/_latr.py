
import MySQLdb
import hug

import constants
from constants import sql_templates
import falcon

from Resources import Game, User
from db import cnx

#!!!!: NB: This is the outdated Hug API, which I've deprecated in favor of
# Flask. So there's not much reason to kep it around.

# /user
# POST /user?<username> Create user
# GET  /user/{user_id} Get a given user object
# POST /user/{user_id}/{game_id} Join a game
# DEL  /user/{user_id}/{game_id} Leave a game
#
# GET /game/{game_id} Get / poll a game
# PUT /game/{game_id}?<move> Make a move. Maybe hold body in req body?
# POST /game/{user_id} Create and join a new game

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

@hug.get('/game/{game_id}')
def get_game(game_id):
    game = Game(game_id)
    return game.read()

@hug.post('/game/{user_id}')
def create_game(user_id):
    game = Game()
    user = User(user_id)
    user.join(game)
    return game.read()

@hug.post('/home')
def post_method():
    return "you used a post method!"
