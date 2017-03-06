from string import ascii_lowercase


def convert_alg_to_point(coord, board_width, board_height):
    col = int(ascii_lowercase.find(coord[0])) + 1 # dummy col
    row = int(coord[1:])
    if not 0 < col <= board_width:
        raise ValueError('bad coord; invalid col in ' + coord)
    if not 0 < row <= board_height:
        raise ValueError('bad coord; invalid row in ' + coord)
    return row*(board_width + 2) + col

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

def validate_move(game, move_start, move_end, jumps=None):
    """
    Validates move. Checks that check_piece_arrival returns true,
    that move start and end are valid, and that start is occupied.
    Then, if jumps, validates all jumps. If no jumps, checks is_backwards if not
    allow_backwards and then checks check_adjacent.
    """
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
