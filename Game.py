# from db import cnx
import constants
from game_class import GameState
from string import Template
import MySQLdb
cnx = MySQLdb.connect(host="localhost", user="igoinu", passwd="password", db="latr")
queries = {
"create_game": """INSERT INTO game (initial_fen) "{initial_fen}";""",
"get_game": """""",
"get_participants": """SELECT * FROM participant WHERE game_id = {game_id}"""
}


class Participant:
    def __init__(self, participant_id):
        pass

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
        query = self.query_templates["create"].substitute(options)
        cur = cnx.cursor()
        cur.execute(query)
        # raise ValueError("bang", row)
        cnx.commit()
        cur.execute("SELECT LAST_INSERT_ID();")
        self.resource_id = cur.fetchone()[0]
        # print("row", row)
        cur.close()

    def read(self):
        """ Read resource """
        query = self.query_templates["read"].substitute(resource_id=self.resource_id)
        cur = cnx.cursor()
        cur.execute(query)
        cnx.commit()
        row = dict(zip(self.resource_cols, cur.fetchone()))
        cur.close()
        return row

    def delete(self):
        """ Have a resource delete itself """
        query = self.query_templates["delete"].substitute(resource_id=self.resource_id)
        cur = cnx.cursor()
        cur.execute(query)
        cnx.commit()
        cur.close()


class Game(Resource):
    query_templates = {
    "create": Template("""INSERT INTO game (initial_fen) VALUES ("$initial_fen");"""),
    "read": Template("""SELECT * FROM game WHERE game_id = $resource_id"""),
    "delete": Template("""DELETE FROM game WHERE game_id = $resource_id"""),
    "get_moves": Template("""SELECT * FROM move WHERE game_id = $resource_id ORDER BY half_move_clock"""),
    "get_participants": Template("""SELECT * FROM participant WHERE game_id = $resource_id"""),
    "join": Template("""INSERT INTO participant (user_id, game_id, color) VALUES ($user_id, $game_id, $color)"""),
    "add_move": Template("""INSERT INTO move (game_id, participant_id, fen, half_move_clock, notation) VALUES ($game_id, $participant_id, "$fen", $half_move_clock, "$notation")""")
    }
    default_options = {"initial_fen": "c/c/c/c/c/c/c/c,0,0,0 12,8,12,d,-4,T o/1110/1121/2/f"}
    move_cols = ("move_id", "game_id", "participant_id", "fen", "half_move_clock", "notation")
    user_cols = ("participant_id", "user_id", "game_id", "color")
    resource_cols = ("game_id", "start_time", "initial_fen")

    @property
    def moves(self):
        cur = cnx.cursor()
        query = self.query_templates["get_moves"].substitute(resource_id=self.resource_id)
        cur.execute(query)
        moves = [dict(zip(self.move_cols, row)) for row in cur.fetchall()]
        cur.close()
        return moves

    @property
    def participants(self):
        cur = cnx.cursor()
        query = self.query_templates["get_participants"].substitute(resource_id=self.resource_id)
        cur.execute(query)
        moves = [dict(zip(self.user_cols, row)) for row in cur.fetchall()]
        cur.close()
        return moves

    def join(self, user_id, color=-1):
        cur = cnx.cursor()
        values = {"user_id": user_id, "game_id": self.resource_id, "color": color}
        query = self.query_templates["join"].substitute(values)
        # raise ValueError(query)
        cur.execute(query)
        cur.close()

    def make_move(self, participant_id, move):
        cur = cnx.cursor()
        # Need some kind of more thorough veting to make sure the right user is making moves?
        color = [participant["color"] for participant in self.participants if participant.user_id == user_id][0]
        game_state = GameState(self.moves[-1]["fen"])
        game_state.handle_move(move)
        values = dict(zip(("game_id", "participant_id", "fen", "half_move_clock", "notation"), (self.resource_id, participant_id, game_state.fen_string, game_state.half_move, move)))
        query = self.query_templates["make_move"].substitute(values)
        cur.execute(query)
        cur.close()
