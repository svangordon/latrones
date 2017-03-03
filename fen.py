""" various methods for handling the creation, manipulation, and validation of FEN strings """

from string import Template

def create_fen(board_width=12, board_height=8):
    # [position string] [board_width] [board_height] [active_player in w|b] [stone_count] [gamePhase in d|m] [half_move_clock] [full_move_clock]
    position_string = '/'.join([str(board_width)] * board_height)
    return Template("$position_string $board_width $board_height w 0 0 1").substitute(locals())

def deserialize_fen_string(fen_input:str):
    """ Return a dict representing the FEN for python """
    columns = ('board_string', 'board_width', 'board_height', 'active_player', 'stone_count', 'half_move_clock', 'full_move_clock')
    def fen_map(chunk):
        try:
            return int(chunk)
        except (ValueError, TypeError):
            return chunk
    fen_dict = dict(zip(columns, map(fen_map, fen_input.split(' '))))
    fen_dict['board_string'] = deserialize_board_string(fen_dict["board_string"])
    return fen_dict
    # fen_dict["board_string"] = deserialize_board_string(fen_dict["board_string"])
    # fen_dict["board_width"] = int(fen_dict["board_width"])
    # fen_dict["board_height"] = int(fen_dict["board_height"])
    # fen_dict["active_player"] = int(fen_dict["active_player"])

def deserialize_board_string(fen_input:str):
    """ Return a list of dicts representing the game board"""
    # fen_dict = dict(zip(('board_string', 'board_width', 'board_height', 'active_player', 'stone_count', 'gamePhase', 'half_move_clock', 'full_move_clock') ,fen_input.split(' ')))
    board_width = 2 # add one on each side
    passed_one = False
    for char in fen_input.split('/')[0]:
        try:
            board_width += int(char)
            if passed_one:
                board_width += 9
            passed_one = int(char) == 1
        except ValueError:
            board_width += 1
            passed_one = false
    # print(board_width)

    output_board = [generate_square(-1)] * board_width
    output_board.extend([item for sublist in map(deserialize_row, fen_input.split('/')) for item in sublist])
    output_board.extend([generate_square(-1)] * board_width)

    return output_board

def deserialize_row(row_input):
    output_row = [generate_square(-1)]
    # print(len(row_input))
    for char in row_input:
        output_row.extend(deserialize_char(char))
    output_row.extend([generate_square(-1)])
    return output_row

def deserialize_char(char_input):
    """ Should never be passed -1, I don't think """
    if char_input == str(-1):
        raise TypeError("deserialize_char passed -1")
    try:
        return int(char_input) * [generate_square(None)]
    except ValueError as e:
        # print('received {0}'.format(char_input))
        return [generate_square(char_input)]


def generate_square(char=None):
    """ Pass -1 for non-valid squares """
    # print('generate_square received', char)
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
        raise ValueError('invalid char ', char)

    if char.isupper():
        output["checked"] = True
    return output

def generate_char(square):
    if not square["valid"]:
        return ''
    if not square["occupied"]:
        return '1' #down the line we'll reduce all the nums
    output = ''
    if square["owner"] == 0:
        output = 'w'
    elif square["owner"] == 1:
        output = 'b'
    else:
        raise ValueError('invalid owner value')
    if square["checked"]:
        output = output.upper()
    return output

def serialize_fen_string(fen_object):
    # [position string] [board_width] [board_height] [active_player in w|b] [stone_count] [gamePhase in d|m] [half_move_clock] [full_move_clock]
    fen_template = Template("$board_string $board_width $board_height $active_player $stone_count $half_move_clock $full_move_clock")
    fen_object["board_string"] = serialize_board_string(fen_object["board_string"])
    return fen_template.substitute(fen_object)

def serialize_board_string(board_list):
    output = []
    passed_invalid = False
    entered_board = False
    empty_count = 0
    for square in board_list:
        if not square['valid']:
            passed_invalid = True
            if empty_count != 0:
                output.extend(str(empty_count))
            empty_count = 0
            # continue
        elif square["valid"]:
            if passed_invalid:
                passed_invalid = False
                if not entered_board:
                    entered_board = True
                else:
                    output.extend('/') # probably need to move delimiters to constants
            if not square["occupied"]:
                empty_count += 1
            elif square["occupied"]:
                if empty_count != 0:
                    output.extend(str(empty_count))
                    empty_count = 0
                output.extend(generate_char(square))
            else:
                raise ValueError("fell through unexpectedly")
            # output.extend(generate_char(square))
        else:
            raise ValueError('fell through unexpectedly')
    return ''.join(output)
