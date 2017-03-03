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

def validate_move(game_object, move_from, move_to):
    """ Return Bool for whether a given move is legal """
    origin_point = convert_alg_to_point(move_from, game_object["board_width"])
    origin = (convert_alg_to_point)
    # Check to make sure
