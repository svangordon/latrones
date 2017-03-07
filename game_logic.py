from string import ascii_lowercase
from fen import serialize_fen_string, deserialize_fen_string

def convert_alg_to_point(game):
    def curried(coord):
        col = int(ascii_lowercase.find(coord[0])) + 1 # dummy col
        row = int(coord[1:])
        if not 0 < col <= game["board_width"]:
            raise ValueError('bad coord; invalid col in ' + coord)
        if not 0 < row <= game["board_height"]:
            raise ValueError('bad coord; invalid row in ' + coord)
        return row*(game["row_width"]) + col
    return curried

def convert_point_to_alg(coord, board_width, board_height):
    if coord - (board_width + 2) < 0 \
        or coord+(board_width + 2) > (board_width + 2)*(board_height + 2) \
        or coord % (board_width + 2) == 0 \
        or coord % (board_width + 2) == board_width + 1:
            raise ValueError('bad coord; converting invalid point to algebraic' + str(coord))
    col = coord%(board_width + 2) - 1
    row = int(coord / (board_width + 2))
    return ascii_lowercase[col] + str(row)

def is_backwards(game, move_start, move_end):
    """ Return whether a given move is backwards. Only interested in whether
    it is a single step backwards (as opposed to a jump)"""
    row_width = game["row_width"]
    step = -(row_width) if game["active_player"] == 0 else row_width
    return move_start + step == move_end

def validate_jump(game, move_start, move_end):
    """ Return whether a given jump is valid; only looks at the direction. If it is
    a backwards move or jumping piece is checked, checks that jumped piece is friendly.
    Only checks one jump, use multiple calls to check multiple jumps in a turn.
    Checks that end is a valid step from start. Then checks piece arrival (which
    it has to)
    """
    if move_end == move_start + 2:
        jumped_coord = move_start + 1
    elif move_end == move_start - 2:
        jumped_coord = move_start - 1
    elif move_end == move_start - game["row_width"]*2:
        jumped_coord = move_start - game["row_width"]
    elif move_end == move_start + game["row_width"]*2:
        jumped_coord = move_start + game["row_width"]
    else:
        raise ValueError("Bad jump coord")
    start_square = game["board"][move_start]
    jumped_square = game["board"][jumped_coord]

    if not check_piece_arrival(game, move_start, move_end):
        raise ValueError("Bad piece arrival")
        return False
    if not game["rules"]["allow_jump_enemy_backwards"] \
    and not start_square["owner"] == jumped_square["owner"] \
    and is_backwards(game, move_start, jumped_coord):
        raise ValueError("jumping backwards over enemey")
        # return False
    if start_square["checked"] and not start_square["owner"] == jumped_square["owner"]:
        raise ValueError("Checked piece jumping non-friendly piece")
        # return False
    return True

def check_adjacent(game, central_square, *squares):
    """ Returns if all args are adjacent to central_square.
    come to think of it, why would this need to accept multiple squares? """
    row_width = game["board_width"] + 2
    if len(squares) > 4:
        raise ValueError("too many squares passed to check_adjacent")
    for square in squares:
        int(square)
        if square not in [central_square + 1, central_square - 1,
        central_square + row_width, central_square - row_width]:
            return False
    return True

def check_attr(game, attr, expected, *squares):
    """ Check whether attr of squares == expected """
    valid_attr = ["occupied", "checked", "owner", "valid"]
    # handle a list, if passed
    try:
        squares = list(squares[0])
    except TypeError:
        pass
    if not attr in valid_attr:
        raise ValueError("bad attr {0}".format(attr))
    row_width = game["board_width"] + 2
    for square in squares:
        if not game["board"][square][attr] == expected:
            return False
    return True

def check_piece_arrival(game, move_start, move_end):
    """ checks whether a piece can legally arrive at its destination square,
        based solely on the contents of the origin and dest squares. Returns Bool.
        Checks that start and end are valid, check that start is occupied.
        If end is occupied, checks that end piece is different from moving player,
        and that it's checked, and that displacement capture is allowed.
    """
    start_square = game["board"][move_start]
    end_square = game["board"][move_end]
    # probably kill this
    if not check_attr(game, "valid", True, move_start, move_end):
        raise ValueError("checking arrival for invalid squares")
    if not check_attr(game, "occupied", True, move_start):
        raise ValueError("attempting to move from invalid square")
    if check_attr(game, "occupied", True, move_end):
        if check_attr(game, "owner", start_square["owner"], move_start, move_end):
            return False
        if game["rules"]["displacement_capture"]: #NB: as of writing, the rules dict hasn't actually been added
            return check_attr(game, "checked", True, move_end)
        return False
    return True

def validate_move(game, *squares):
    """
    Validates move. Checks that check_piece_arrival returns true,
    that move start and end are valid, and that start is occupied.
    Then, if jumps, validates all jumps. If no jumps, checks is_backwards if not
    allow_backwards and then checks check_adjacent.
    """
    move_start = squares[0]
    move_end = squares[-1]
    jumps = squares[1:-1]
    if not (check_piece_arrival(game, move_start, move_end) and \
    check_attr(game, "valid", True, move_start, move_end) and \
    check_attr(game, "occupied", True, move_start)):
        return False
    if jumps:
        for jump in jumps:
            if not validate_jump(game, *jump):
                return False
    else:
        if not game["rules"]["allow_backwards"] and \
        is_backwards(game, move_start, move_end) or \
        not check_adjacent(game, move_start, move_end):
            return False
    return True

# def make_move(game, move_start, move_end):
#     """
#     Return a new game object, updated for the move. Does not validate.
#     """
#     def is_checking(game, piece):
#         """ Return coords for which a piece is part of the only pair checking """
#         # square to check if occupied, square to check if friendly & not checked, two squares to check not friendly & not checked
#         to_check = [
#         (piece + 1, piece + 2, piece+1 - game["row_width"], piece+1 + game["row_width"]),
#         (piece - 1, piece - 2, piece-1 - game["row_width"], piece-1 + game["row_width"]),
#         (piece - game["row_width"], piece - game["row_width"]*2, piece-game["row_width"] - 1, piece-game["row_width"] + 1),
#         (piece + game["row_width"], piece + game["row_width"]*2, piece+game["row_width"] - 1, piece+game["row_width"] + 1)
#         ]
#         results = []
#         for squares in to_check:
#             if check_attr(game, "occupied", True, squares[0]) \
#             and not check_attr(game, "owner", game["board"][piece]["owner"], squares[0]) \
#             and check_attr(game, "owner", game["board"][piece]["owner"], squares[1]) \
#             and check_attr(game, "checked", False, squares[1]) \
#             and not (check_attr(game, "owner", game["board"][piece]["owner"], squares[2], squares[3]) and check_attr(game, "checked", False, squares[2], squares[3])):
#                 results.extend(squares[0])
#         return results
#
#     if game["rules"]["check"]:

def is_checking(game, piece, only_checker=False):
    """ Return coords for which a piece is checking, with flag for if we want
    stones for which it is part of the only pair checking """
    # square to check if occupied, square to check if friendly & not checked, two squares to check not friendly & not checked
    to_check = [
    (piece + 1, piece + 2, piece+1 - game["row_width"], piece+1 + game["row_width"]),
    (piece - 1, piece - 2, piece-1 - game["row_width"], piece-1 + game["row_width"]),
    (piece - game["row_width"], piece - game["row_width"]*2, piece-game["row_width"] - 1, piece-game["row_width"] + 1),
    (piece + game["row_width"], piece + game["row_width"]*2, piece+game["row_width"] - 1, piece+game["row_width"] + 1)
    ]
    results = []
    for squares in to_check:
        if check_attr(game, "occupied", True, squares[0]) \
        and not check_attr(game, "owner", game["board"][piece]["owner"], squares[0]) \
        and check_attr(game, "owner", game["board"][piece]["owner"], squares[1]) \
        and check_attr(game, "checked", False, squares[1]) \
        and not (only_checker and check_attr(game, "owner", game["board"][piece]["owner"], squares[2], squares[3]) and check_attr(game, "checked", False, squares[2], squares[3])):
            results.append(squares[0])
    return results

def is_opposing(game, square1, square2):
    """ Returns whether squares are both occupied and have dif owners """
    return check_attr(game, "occupied", True, square1, square2) and not check_attr(game, "owner", game["board"][square1]["owner"], square2)

def is_friendly(game, square1, square2):
    """ Return whether both occupied and same owner """
    return check_attr(game, "occupied", True, square1, square2) and check_attr(game, "owner", game["board"][square1]["owner"], square2)

def check_sandwiches(game, square, opt=None):
    """ returns coord for squares of enemy pieces square is sandwiching """
    possible_partners = [square + 1, square - 1, square + game["row_width"], square - game["row_width"]]

def is_sandwiched(game, square):
    """ returns int for number of pairs of enemy pieces sandwiching square """
    pairs = [(square - 1, square + 1), (square - game["row_width"], square + game["row_width"])]
    results = []
    for pair in pairs:
        if is_opposing(game, square, pair[0]) and is_friendly(game, *pair) \
        and (not game["rules"]["check"] or check_attr(game, "checked", False, *pair)):
            results.append(pair)
    return results

def clear_square(game, square):
    game["board"][square] = {
        "occupied": False,
        "checked": False,
        "owner": -1,
        "valid": True
    }

def modify_game(game, move_start, move_end):
    """ Returns modified game object w/ given move made """
    if game["rules"]["check"]:
        for square in is_checking(game, move_start, True):
            game["board"][square]["checked"] = False
    game["board"][move_end] = dict(game["board"][move_start])
    # empty source square
    clear_square(game, move_start)
    neighbors = is_checking(game, move_end)
    for neighbor in neighbors:
        if game["rules"]["custodial_capture"]:
            clear_square(game, neighbor)
        if game["rules"]["check"]:
            game["board"][neighbor][checked] = True
            for square in is_checking(game, neighbor, True):
                game["board"][square]["checked"] = False
    return game

def make_move(fen_string, move_string):
    game = deserialize_fen_string(fen_string)
    moves = list(map(convert_alg_to_point(game), move_string.split(' ')))
    if not validate_move(game, *moves):
        raise ValueError("Invalid move")
    return serialize_fen_string(modify_game(game, moves[0], moves[-1]))
