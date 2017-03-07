class GameState:

    fen_strings = {
        "standard": "12/12/12/12/12/12/12/12,12,8,w,0,0,1 d,-4,T o/1101/1121/2222/2/f" #seperate pieces w/ comma
    }

    def __init__(self, arg1, init=False):
        self.board = []
        self.rules = {}
        self.pieces = {}
        if init:
            self.deserialize_fen_string(self.fen_strings[arg1])
        else:
            self.deserialize_fen_string(arg1)

    def deserialize_fen_string(self, fen_string):
        split_string = fen_string.split(' ')
        board = split_string[0]
        rules = split_string[1]
        pieces = split_string[2]
        neg_flag = False
        for char in rules:
            if char == "-":
                neg_flag = True
                continue

    def deserialize_rules(self, rule_string):
        rules = rule_string.split(',')
        capture_methods = {
            "d": "displacement",
            "c": "custodial",
            "dC": "delayed_custodial"
        }
        trapping = {
            "T": True,
            "t": False
        }
        self.rules["capture_method"] = capture_methods[rules[0]]
        self.rules["win_condition"] = int(rules[1])
        self.rules["trapping"] = trapping[rules[2]]

    def serialize_rules(self):
        rules = []
        capture_methods = {
            "displacement": "d",
            "custodial": "c",
            "delayed_custodial": "dC"
        }
        trapping = {
            True: "T",
            False: "t"
        }
        rules.append(capture_methods[self.rules["capture_method"]])
        rules.append(str(self.rules["win_condition"]))
        rules.append(trapping[self.rules["trapping"]])
        return ','.join(rules)

    def deserialize_pieces(self, pieces_string):
        """ the pieces_string into a dictionary of PieceGenerators """
        pieces_dict = {}
        for piece_string in pieces_string.split(','):
            pieces_dict[piece_string[0]] = PieceGenerator(self, piece_string)
        self.pieces_dict = pieces_dict

    def serialize_pieces(self):
        output = []
        for piece in self.pieces_dict:
            output.append(self.pieces_dict[piece].piece_string)
        return ','.join(output)


class PieceGenerator:
    """ piece_string: char, free_move, free_jump, trapped_jump, surrounding_pairs_to_capture, lose_on_capture
                     o/1101/1121/2222/2/f
         can generate pieces, obviously
     """
    def __init__(self, game, piece_string):
        fields = piece_string.split('/')
        self.piece_string = piece_string
        self.char = fields[0]
        self.move = fields[1].split()
        self.free_jumps = fields[2].split()
        self.trapped_jumps = fields[3].split()
        self.sides_to_capture = fields[4]
        self.lose_on_capture = fields[5]
        self.props = {
                "char": fields[0],
                "move": fields[1].split(),
                "free_jumps": fields[2].split(),
                "trapped_jumps": fields[3].split(),
                "sides_to_capture": fields[4],
                "lose_on_capture": fields[5]
        }
        self.game = game

    def create_piece(self, owner, position):
        props = dict(self.props)
        props["owner"] = owner
        props["position"] = position
        return GamePiece(self.game, props)

class GamePiece:
    def __init__(self, game, props):
        self.props = props
        self.game = game
