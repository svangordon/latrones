class GameState:

    fen_strings = {
        "standard": "12/12/12/12/12/12/12/12,12,8,w,12,0,0,1 d,-4,T o/1101/1121/2222/2/f" #seperate pieces w/ comma
    }

    cols = ('board', 'board_width', 'board_height', 'active_player', 'stone_count', 'half_move_clock', 'full_move_clock')

    def __init__(self, fen_string, init=False):
        self.turn = {}
        self.rules = {}
        self.pieces = {}
        if init:
            fen_string = fen_strings[fen_string]
        split_string = fen_string.split(' ')
        # board = split_string[0]
        # rules = split_string[1]
        # pieces = split_string[2]
        self.board_string = split_string[0]
        self.rules_string = split_string[1]
        self.pieces_string = split_string[2]
        self.deserialize_rules()
        self.deserialize_pieces()
        self.deserialize_turn()
        # self.deserialize_rules(rules)
        # self.deserialize_pieces(pieces)


    # def deserialize_fen_string(self, fen_string):

    def deserialize_rules(self):
        rules = self.rule_string.split(',')
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

    def deserialize_pieces(self):
        """ add all of the piece strings into self.gen """
        pieces_dict = {}
        self.gen = PieceGenerator(self)
        for piece_string in self.pieces_string.split(','):
            self.gen.add_piece(piece_string)
            # pieces_dict[piece_string[0]] = PieceGenerator(self, piece_string)
        # self.pieces_dict = pieces_dict

    def serialize_pieces(self):
        output = []
        for piece in self.pieces_dict:
            output.append(self.pieces_dict[piece].piece_string)
        return ','.join(output)

    def deserialize_turn(self):
        # ('board', 'board_width', 'board_height', 'active_player', 'stone_count', 'half_move_clock', 'full_move_clock')
        # fen_chunks = board_string.split(',')
        def fen_map(chunk):
            try:
                return int(chunk)
            except (ValueError, TypeError):
                return chunk

        # def deserialize_board_string(board_string)

        self.turn = dict(zip(self.columns, map(fen_map, self.turn_string.split(','))))
        self.deserialize_board_string()

    def deserialize_board_string(self):
        output = []
        board_string = self.turn.board
        passed_one_flag = False
        coord_counter = 0
        def add_square(square_type):
            output.append(self.gen.piece(square_type), coord_counter)
            coord_counter += 1
        for i in range(self.turn.row_len):
            add_square("invalid")
        for row in board_string.split('/'):
            add_square("invalid")
            for char in row:
                try:
                    squares_to_add = int(char)
                    if passed_one_flag:
                        squares_to_add += 10
                        passed_one_flag = False
                    elif int(char) == 1:
                        passed_one_flag = True
                    for i in range(squares_to_add):
                        add_square("empty")
                except ValueError:
                    passed_one_flag = False
                    add_square(char)
            add_square("invalid")
        for i in range(self.turn.row_len):
            add_square("invalid")
        # And now, overwrite state
        self.game.turn.board = output


class PieceGenerator:
    """ holds a reference to game, spits out different types of pieces """
    def __init__(self, game):
        self.game = game
        self.pieces = {
            "invalid": {
                "invalid": True,
                "occupied": False
            },
            "empty": {
                "invalid": False,
                "occupied": False
            }
        }

    def add_piece(self, char, input_props):
        props = dict(input_props)
        props["empty"] = False
        props["invalid"] = False
        self.pieces[char] = props

    def piece(self, piece_name, position):
        props = dict(self.pieces[piece_name])
        return GamePiece(game, props, position)

class GamePiece:
    def __init__(self, game, props, position):
        self.props = props
        self.game = game
