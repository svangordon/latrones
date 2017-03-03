from string import ascii_lowercase

# def validate_move(game_object, move_to, move_from=None):
#     """ Return Bool for whether a given move is legal """
#     if move_from is not None and game_object["gamePhase"] != 'm'
#             return False
#     elif move_from is not None game_object["gamePhase"] == 'd

def convert_alg_to_point(coord, board_width, board_height):
    col = int(ascii_lowercase.find(coord[0])) + 1 # dummy col
    row = int(coord[1:])
    if not 0 < col <= board_width:
        raise ValueError('bad coord; invalid col in ' + coord)
    if not 0 < row <= board_height:
        raise ValueError('bad coord; invalid row in ' + coord)
    return row*(board_width + 2) + col
