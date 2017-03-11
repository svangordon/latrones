# from db import cnx
import constants
from game_class import GameState
from string import Template
import MySQLdb
from db import cnx
# cnx = MySQLdb.connect(host="localhost", user="igoinu", passwd="password", db="latr")
from pprint import pprint


class Resource:
    def __init__(self, resource_id=None, options=None):
        if not options:
            options = self.default_options
        if not resource_id:
            self.create(options)
        else:
            self.resource_id = resource_id

    def create(self, options):
        """ Create a resource, and then return it (or maybe its id idk) """
        query = self.queries["create"].substitute(options)
        cur = cnx.cursor()
        cur.execute(query)
        # raise ValueError("bang", row)
        cnx.commit()
        cur.execute("SELECT LAST_INSERT_ID();")
        self.resource_id = cur.fetchone()[0]
        cur.close()

    def read(self, query_template="read"):
        """ Read resource """
        query = self.queries[query_template].substitute(resource_id=self.resource_id)
        cur = cnx.cursor()
        cur.execute(query)
        cnx.commit()
        row = dict(zip(self.resource_cols, cur.fetchone()))
        cur.close()
        return row

    def delete(self, query_template="delete"):
        """ Have a resource delete itself """
        cur = cnx.cursor()
        if isinstance(self.queries[query_template], list):
            for template in self.queries[query_template]:
                query = template.substitute(resource_id=self.resource_id)
                cur.execute(query)
                cnx.commit()
        else:
            query = self.queries[query_template].substitute(resource_id=self.resource_id)
            cur.execute(query)
            cnx.commit()
        cur.close()

class Participant(Resource):
    queries = {
        "join": Template("""INSERT INTO participant (user_id, game_id, color) VALUES ($user_id, $game_id, $color)"""),
        "leave": Template("""DELETE FROM participant WHERE game_id = $game_id AND user_id = $user_id""")
    }
    def __init__(self, user_id):
        self.user_id = user_id
    def join(self, game_id, color=-1):
        cur = cnx.cursor()
        values = {"user_id": self.user_id, "game_id": game_id, "color": color}
        query = self.queries["join"].substitute(values)
        cur.execute(query)
        cnx.commit()
        cur.execute("SELECT LAST_INSERT_ID();")
        self.game_id = cur.fetchone()[2]
        cur.close()
    def leave(self, game_id=None):
        if not game_id:
            game_id = self.game_id
        cur = cnx.cursor()
        values = {"user_id": self.user_id, "game_id": game_id, "color": color}
        query = self.queries["leave"].substitute(values)
        cur.execute(query)
        cnx.commit()
        cur.close()

class User(Resource):
    queries = {
    "create": Template("""INSERT INTO user (username) VALUES ("$username");"""),
    "get_active_games": Template("""SELECT game.game_id, start_time, initial_fen, game_status FROM game LEFT JOIN (participant)
	ON (game.game_id = participant.game_id AND participant.user_id = $user_id AND (game.game_status = 0 OR game.game_status = 1)) """)
    "delete": Template("""DELETE FROM user WHERE user_id = $resource_id"""),
    "get__by_username": Template("""SELECT * FROM user WHERE username = $identifier"""),
    "get_by_id": Template("""SELECT * FROM user WHERE user_id = $identifier""")
    }
    resource_cols = ("user_id", "username")
    def __init__(self, user_identifier=None):
        """ they identifier is either the username or userstring """
        # self.resource_id = user_id
        if user_identifier:
            user = self.read(user_identifier)
            self.resource_id = user["user_id"]
            self.username = user["username"]

    def read(self, identifier=None):
        if identifier is None:
            identifier = self.user_id
        cur = cnx.cursor()
        try:
            query = self.queries["get_by_id"].substitute(identifier=int(identifier))
        except ValueError:
            # identifier == str
            query = self.queries["get_by_username"].substitute(identifier=identifier)
        cur.execute(query)
        row = dict(zip(self.resource_cols, cur.fetchone()))
        return row
        # user_data = cur.fetchone()
        # self.user_id = user_data[0]
        # self.username = user_data[1]

    @property
    def profile(self):
        """ Imaginary profile ish goes here """
        if not self.resource_id:
            raise ValueError("attempting to get profile but no resource_id")
        return "I haven't actually decided what data the profile needs" # Rating, nationality, name, profile pic, last ten games, maybe

    @property
    def active_games(self):
        cur = cnx.cursor()
        if not self.user_id:
            return None # maybe throw an error?
        query = self.queries["get_active_games"].substitute(user_id=self.resource_id)
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        return [Game(row) for row in rows]

    @property
    def username(self):
        """ Probably, I should be caching this """
        cur = cnx.cursor()
        query = self.queries["get_username"].substitute(resource_id=self.resource_id)
        cur.execute(query)
        username = cur.fetchone()[0]
        cur.close()
        return username

class Game(Resource):
    queries = {
    "create": Template("""INSERT INTO game (initial_fen, game_status) VALUES ("$initial_fen", 0);"""),
    "read": Template("""SELECT * FROM game WHERE game_id = $resource_id"""),
    "delete": [Template("""DELETE FROM participant WHERE game_id = $resource_id;"""),
    Template("""DELETE FROM move WHERE game_id = $resource_id;"""),
    Template("""DELETE FROM game WHERE game_id = $resource_id;""")], # this totally scrubs it from the db. For other kinds of resources, a gentler behavior might be desirable
    "get_moves": Template("""SELECT * FROM move WHERE game_id = $resource_id ORDER BY half_move_clock"""),
    "get_participants": Template("""SELECT * FROM participant WHERE game_id = $resource_id"""),
    "join": Template("""INSERT INTO participant (user_id, game_id, color) VALUES ($user_id, $game_id, $color)"""),
    "make_move": Template("""INSERT INTO move (game_id, participant_id, fen, half_move_clock, notation) VALUES ($game_id, $participant_id, "$fen", $half_move_clock, "$notation")""")
    }
    default_options = {"initial_fen": "oooooooooooo/c/c/c/c/c/c/OOOOOOOOOOOO,0,0,0 12,8,12,d,-4,T o/0111/2111/2/f"}
    move_cols = ("move_id", "game_id", "participant_id", "fen", "half_move_clock", "notation")
    user_cols = ("participant_id", "user_id", "game_id", "color")
    resource_cols = ("game_id", "start_time", "initial_fen")

    @property
    def moves(self):
        cur = cnx.cursor()
        query = self.queries["get_moves"].substitute(resource_id=self.resource_id)
        cur.execute(query)
        moves = [dict(zip(self.move_cols, row)) for row in cur.fetchall()]
        cur.close()
        return moves

    @property
    def participants(self):
        cur = cnx.cursor()
        query = self.queries["get_participants"].substitute(resource_id=self.resource_id)
        cur.execute(query)
        moves = [dict(zip(self.user_cols, row)) for row in cur.fetchall()]
        cur.close()
        return moves

    def join(self, user_id, color=-1):
        cur = cnx.cursor()
        values = {"user_id": user_id, "game_id": self.resource_id, "color": color}
        query = self.queries["join"].substitute(values)
        # raise ValueError(query)
        cur.execute(query)
        cur.close()

    def make_move(self, user_id, move):
        cur = cnx.cursor()
        participant_id = [participant for participant in self.participants if participant["user_id"] == user_id][0]["participant_id"]
        # Need some kind of more thorough veting to make sure the right user is making moves?
        color = [participant["color"] for participant in self.participants if participant["user_id"] == user_id][0]
        try:
            game_state = GameState(self.moves[-1]["fen"])
        except IndexError:
            game_state = GameState(self.read()["initial_fen"])
        game_state.handle_move(move)
        values = dict(zip(("game_id", "participant_id", "fen", "half_move_clock", "notation"), (self.resource_id, participant_id, game_state.fen_string, game_state.turn["half_move_clock"], move)))
        query = self.queries["make_move"].substitute(values)
        cur.execute(query)
        cnx.commit()
        cur.close()


    # def begin_game(self):
    #     if
