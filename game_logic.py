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

def validate_move(game_object, move_from, move_to, jumps=None):
    """ Return Bool for whether a given move is legal """
    board_dim = (game_object["board_width"], game_object["board_height"])
    origin_point = convert_alg_to_point(move_from, *board_dim)
    origin_square = game_object["board"][origin_point]
    dest_point = convert_alg_to_point(move_to, *board_dim)
    dest_square = game_object["board"][dest_point]
    # origin square should be owned by active player
    if origin_square["owner"] != game_object["active_player"]:
        return False

    # dest square should be valid
    if not dest_square["valid"]:
        return False

def is_backwards(move_start, move_end, active_player, board_width):
    """ Return whether a given move is backwards. Only interested in whether
    it is a single step backwards (as opposed to a jump)"""
    step = -(board_width+2) if active_player == 0 else board_width+2
    return move_start + step == move_end

def validate_jump(start_coord, jumped_coord, end_coord, game_object):
    """ Return whether a given jump is valid; only looks at the direction. If it is
    a backwards move or jumping piece is checked, checks that jumped piece is friendly.
    Only checks one jump, use multiple calls to check multiple jumps in a turn"""
    start_square = game_object["board"][start_coord]
    jumped_square = game_object["board"][jumped_coord]
    end_square = game_object["board"][end_coord]
    row_len = game_object["board_width"] + 2

    # if jump is backwards or jumping piece is checked, jumped piece must be friendly
    if (is_backwards(start_coord, jumped_coord, game_object["active_player"], game_object["board_width"]) \
        or start_square["checked"]) and \
        not start_square["owner"] == jumped_square["owner"]:
            return False
    coord_valid = (start_coord == jumped_coord + 1 and start_coord == end_coord + 2) or \
        (start_coord == jumped_coord -1 and start_coord == end_coord -2) or \
        (start_coord == jumped_coord - row_len and start_coord == end_coord - row_len*2) or \
        (start_coord == jumped_coord + row_len and start_coord == end_coord + row_len*2)
    return coord_valid and jumped_square["owner"] != -1 and (end_square["checked"] or end_square["owner"] == -1) and end_square["valid"] == True

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
