""" various methods for handling the creation, manipulation, and validation of FEN strings """

from string import Template

def create_fen(board_width, board_height):
    # [position string] [boardWidth] [boardHeight] [activePlayer in w|b] [stoneCount] [gamePhase in d|m] [halfmoveClock] [fullMoveClock]
    position_string = '/'.join([str(board_width)] * board_height)
    return Template("$position_string $board_width $board_height w 0 d 0 1").substitute(locals())

def deserialize_fen_string(fen_input:str):
    """ Return a list of dicts representing the game board"""
    fen_dict = dict(zip(('boardString', 'boardWidth', 'boardHeight', 'activePlayer', 'stoneCount', 'gamePhase', 'halfmoveClock', 'fullMoveClock') ,fen_input.split(' ')))
    # input_board = fen.split(' ')[0].split('/')
    output_board = [char_generator(-1)] * int(fen_dict["boardWidth"])

    output_board.extend(map(deserialize_row, fen_dict["boardString"].split('/')))

    output_board.extend([char_generator(-1)] * int(fen_dict["boardWidth"]))

    return output_board

def deserialize_row(row_input):
    output_row = [char_generator(-1)]
    for char in list(row_input):
        output_row.extend(deserialize_char(char))
    output_row.extend([char_generator(-1)])
    return output_row

def deserialize_char(char_input):
    """ Should never be passed -1, I don't think """
    if char_input == str(-1):
        raise TypeError("deserialize_char passed -1")
    try:
        return int(char_input) * [char_generator(None)]
    except ValueError as e:
        return [char_generator(char_input)]


def char_generator(char=None):
    """ Pass -1 for non-valid squares """
    output = {
        "occupied": False,
        "checked": False,
        "owner": -1,
        "valid": False
    }
    if char == -1:
        return output
    output["valid"] = True
    if char == None:
        return output
    output["occupied"] = True
    if char.lower() == 'w':
        output["owner"] = 0
    elif char.lower() == 'b':
        output["owner"] = 1
    else:
        raise ValueError('invalid char')

    if char.isupper():
        output["checked"] = True
    return output
