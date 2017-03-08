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
        self.turn_string = split_string[0]
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
        self.board_string = self.turn["board"]
        self.deserialize_board_string()

    def deserialize_board_string(self):
        output = []
        board_string = self.turn.board
        assert isinstance(board_string, str)
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
        self.game.turn["board"] = output

    def serialize_board_string(self):
        output = ''
        pointer = self.turn.row_len + 1
        consecutive_empty = 0
        for i in self.turn.board_height:
            for k in self.turn.board_width:
                if not self.turn.board[pointer]["occupied"]:
                    consecutive_empty += 1
                else:
                    if consecutive_empty:
                        output += str(consecutive_empty)
                        consecutive_empty = 0
                    char = self.turn.board[pointer]["char"]
                    if self.turn.board[pointer]["owner"] == 0:
                        output += self.turn.board[pointer]["char"].lower()
                    else:
                        output += self.turn.board[pointer]["char"].upper()
            if consecutive_empty:
                output += str(consecutive_empty)
                consecutive_empty = 0
            output += '/'
            pointer -= self.turn.board_width
            pointer += self.turn.row_len
        self.board_string = output

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
        self.position = position
        self.occupied = props["occupied"]
        self.valid = props["valid"]
        self.owner = props["owner"]
        self.trapped = props["trapped"]
        self.char = props["char"]
        self.move_pattern = props["move"]
        self.jump_pattern = props["jumps"]
        self.trapped_jump_pattern = props["trapped_jump_pattern"]

    def determine_direction(self, start:int, dest:int):
        """ return which cardinal direction a move is in """
        # row_step is how we'd change coord to go "forward" relative to the piece
        if self.game.turn["active_player"] == 1:
            row_step = -self.game["turn"]["row_len"]
        else:
            row_step = self.game["turn"]["row_len"]
        #determine which direction we're going in (starting at forward, counting clockwise)
        if start - row_step <= dest:
            return 0
        elif start + row_step >= dest:
            return 2
        elif origin_square.position - row_step < end_square.position < origin_square.position:
            return 1 # might be wrong on this?
        elif origin_square.position + row_step > end_square.position > origin_square.position:
            return 3
        else:
            raise ValueError("tried to find direction and failed")

    def make_move(self, *squares):
        self.validate_move(*squares)
        self.remove_piece(squares[0])
        self.add_piece(squares[-1])

    def validate_move(self, *squares):
        board = game.turn["board"]
        origin_square = board[squares[0]]
        end_square = board[squares[-1]]
        if not origin_square["owner"] == self.turn["active_player"]:
            raise ValueError("Moving piece not owned by active_player")

        for square in squares:
            if not board[square]["valid"] == True:
                raise ValueError("Invalid square")

        if len(squares) > 2:
            for i in range(1, len(squares)):
                self.validate_jump(squares[i - 1], squares[i])
        else:
            self.validate_non_jump(*squares)
        # passed all the tests
        return True

    def validate_jump(self, start_coord, end_coord):
        board = game.turn["board"]
        origin_square = board[start_coord]
        end_square = board[end_coord]
        if end_coord == start_square + 2:
            jumped_coord = start_square + 1
        elif end_coord == start_square - 2:
            jumped_coord = start_square - 1
        elif end_coord == start_square - self.game.turn["row_len"]*2:
            jumped_coord = start_square - self.game.turn["row_len"]
        elif end_coord == start_square + self.game.turn["row_len"]*2
            jumped_coord == start_square + self.game.turn["row_len"]
        else:
            raise ValueError("bad jump coord")
        jumped_square = board[jumped_coord]
        direction = self.determine_direction(start_coord, end_coord)

        if jumped_square.owner != self.owner:
            if self.trapped:
                raise ValueError("trapped piece attempting to jump enemy")
            allowed_jump_vals = [1]
        else:
            allowed_jump_vals = [1,2]

        if self.trapped and not self.trapped_jump:
            raise ValueError("trapped piece attempting to jump")

        if self.jump_pattern[direction] not in allowed_jump_vals:
            raise ValueError("bad jump_pattern value", direction, self.jump_pattern[direction])

    def validate_square_entry(self, end_coord):
        """ Validate whether the piece can enter a given square, based on what's already there"""
        end_square = self.game.turn["board"]
        if end_square.occupied:
            if not self.rules["capture_method"] == "displacement":
                raise ValueError("Moving to occupied square, but capture_method != displacement")
            if self.rules["trapping"] and not end_square["trapped"]:
                raise ValueError("Moving to occupied square, but end_square is not trapped")
        if self.game.rules["trapping"] and origin_square["trapped"]:
            raise ValueError("Attmepting to move trapped piece")

        # if self.game.rules["trapping"] and self.trapped:
        #     if self.
        #      and self.trapped_jump_pattern[direction] !== 2:
        #     raise ValueError("jump doesn't fit trapped_jump_pattern")
        # elif self.jump_pattern[direction] !== 1:
        #     raise ValueError("jump doesn't fit jump_pattern")
