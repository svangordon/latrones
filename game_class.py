self.game["rules"]["row_len"]class GameState:

    fen_strings = {
        "standard": "12/12/12/12/12/12/12/12,,w,12,0,0,1 12,8,12,d,-4,T o/1101/1121/2/f" #seperate pieces w/ comma
    }

    turn_cols = ('board', , 'active_player', 'stone_count', 'half_move_clock', 'full_move_clock')
    rules_cols = ('board_width', 'board_height', 'stone_count','capture', 'win_condition', 'trapping')

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
        self.game_string = split_string[0]
        self.rules_string = split_string[1]
        self.pieces_string = split_string[2]
        self.deserialize_rules()
        self.deserialize_pieces()
        self.deserialize_turn()
        # self.deserialize_rules(rules)
        # self.deserialize_pieces(pieces)

    def empty_square(self, square):
        self.turn["board"][square] = self.gen.piece("empty", square)

    def get_square(self, square):
        return self.turn["board"][square]

    def deserialize_rules(self):
        rules = dict(zip(self.rules_cols, self.rules_string.split(',')))
        capture_methods = {
            "d": "displacement",
            "c": "custodial",
            "dC": "delayed_custodial"
        }
        trapping = {
            "T": True,
            "t": False
        }
        rules["board_width"] = int(rules["board_width"])
        rules["board_height"] = int(rules["board_height"])
        rules["stone_count"] = int(rules["stone_count"])
        rules["capture_method"] = capture_methods[rules[0]]
        rules["win_condition"] = int(rules["win_condition"])
        rules["trapping"] = trapping[rules["trapping"]]
        rules["row_len"] = rules["board_width"] + 2
        self.rules = rules

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
        board_string = self.turn["board"]
        assert isinstance(board_string, str)
        passed_one_flag = False
        coord_counter = 0
        def add_square(square_type):
            output.append(self.gen.piece(square_type), coord_counter)
            coord_counter += 1
        for i in range(self.rules["row_len"]):
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
        for i in range(self.rules["row_len"]):
            add_square("invalid")
        # And now, overwrite state
        self.game.turn["board"] = output

    def serialize_board_string(self):
        output = ''
        pointer = self.turn["row_len"] + 1
        consecutive_empty = 0
        for i in self.rules["board_height"]:
            for k in self.rules["board_width"]:
                if not self.turn["board"][pointer]["occupied"]:
                    consecutive_empty += 1
                else:
                    if consecutive_empty:
                        output += str(consecutive_empty)
                        consecutive_empty = 0
                    char = self.turn["board"][pointer]["char"]
                    if self.turn["board"][pointer]["owner"] == 0:
                        output += self.turn["board"][pointer]["char"].lower()
                    else:
                        output += self.turn["board"][pointer]["char"].upper()
            if consecutive_empty:
                output += str(consecutive_empty)
                consecutive_empty = 0
            output += '/'
            pointer -= self.rules["board_width"]
            pointer += self.turn["row_len"]
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

    def determine_direction(self, coord1, coord2=None):
        """ return which cardinal direction a move is in """
        if coord2:
            start = coord_1
            end = coord_2
        else:
            start = self.position
            end = coord_1
        # row_step is how we'd change coord to go "forward" relative to the piece
        if self.game.turn["active_player"] == 1:
            row_step = -self.game["rules"]["row_len"]
        else:
            row_step = self.game["rules"]["row_len"]
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

    def remove_self(self):
        """ The piece removes itself, untrapping if necessary.
        Probably should move this to the game class, but it works here.
        """
        if self.game.rules["trapping"]:
            for trapped_neighbor in [neighbor for neighbor in self.get_neighbors() if neighbor.trapped and self.position in neighbor.get_sandwichers() and len(neighbor.get_sandwichers()) == 2]
                trapped_neighbor.untrap()
        self.game.empty_square(self.position)
        self.position = None

    def add_self(self, square):
        self.position = square
        [neighbor.sandwich() for neighbor in self.get_neighbors() if self.position in neighbor.get_sandwichers()]
        self.game.turn["board"][self.position] = self

    def sandwich(self):
        """ The piece handles itself being sandwiched """
        if self.game.rules["capture_method"] == "custodial_capture":
            self.remove_self()
        if self.game.rules["trapping"]:
            for trapped_neighbor in [neighbor for neighbor in self.get_neighbors() if neighbor.trapped and self.position in neighbor.get_sandwichers() and len(neighbor.get_sandwichers()) == 2]
                trapped_neighbor.untrap()
        self.trap()

    def untrap(self):
        self.trapped = False

    def trap(self):
        [neighbor.untrap() for neighbor in self.neighbors() if  ]
        # self.trapped = True
        # self.checked = True


    def validate_move(self, *squares):
        board = self.game.turn["board"]
        origin_square = board[squares[0]]
        end_square = board[squares[-1]]
        if not origin_square["owner"] == self.turn["active_player"]:
            raise ValueError("Moving piece not owned by active_player")

        if self.game.rules["trapping"] and self.trapped and not len(squares) >= 3:
            raise ValueError("Attmepting to move trapped piece")

        for square in squares:
            if not board[square]["valid"] == True:
                raise ValueError("Invalid square")

        if len(squares) > 2:
            for square in squares [1:-1]:
                if self.game["board"][square]["occupied"]:
                    raise ValueError("attempting to jump through occupied square")
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
        if not end_square.valid:
            raise ValueError("attempting to enter invalid square")
        if end_square.occupied:
            if not self.rules["capture_method"] == "displacement":
                raise ValueError("Moving to occupied square, but capture_method != displacement")
            if self.rules["trapping"] and not end_square["trapped"]:
                raise ValueError("Moving to occupied square, but end_square is not trapped")

    def validate_non_jump(self, end_coord):
        direction = self.determine_direction(end_coord)
        if not self.move_pattern[direction]:
            raise ValueError("attempting non-jump in invalid direction")

        if self.game.turn["active_player"] == 1:
            row_step = -self.game["rules"]["row_len"]
        else:
            row_step = self.game["rules"]["row_len"]
        steps = [row_step, row_step**0, -row_step, -row_step**0] # this order is probably wrong
        step = steps[direction]
        if end_coord != self.position + step and self.move_pattern[direction] != 2:
            raise ValueError("piece with move pattern attempting to move more than 1 space")
        cnt = 1
        while True:
            self.validate_square_entry(self.position + step*cnt)
            if self.position + step*cnt == end_coord:
                break
            elif self.game["board"][self.position + step*cnt].occupied:
                raise ValueError("attempting to move through occupied square")
            cnt += 1
        # we've validated all of the squares, so we're done, i think
        return True

    def get_neighbors(self):
        """ Return list of references to neighboring squares, starting at north and going clockwise """
        return list(map(self.game.get_square, [self.position - self.game.rules["row_len"], self.position + 1, self.position + self.game.rules["row_len"], self.position - 1]))

    def get_sandwichers(self):
        """ returns tuples enemy pieces sandwiching square """
        # pairs = [(square - 1, square + 1), (square - game["row_width"], square + game["row_width"])]
        resultes = []
        neighbors = self.neighbors()
        pairs = ((neighbors[0], neighbors[2]), (neighbors[1], neighbors[3]))
        for pair in pairs:
            if self.owner != pair[0].owner and pair[0].occupied and pair[1].owner == pair[2].owner \
            and (not self.game.rules["trapping"] or True not in [pair[0].trapped, pair[1].trapped]):
                results.append(*pair)
        return results
