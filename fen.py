""" various methods for handling the creation, manipulation, and validation of FEN strings """

from string import Template

def create_fen(board_width, board_height):
    # [position string] [boardWidth] [boardHeight] [activePlayer in w|b] [stoneCount] [gamePhase in d|m] [halfmoveClock] [fullMoveClock]
    position_string = '/'.join([str(board_width)] * board_height)
    return Template("$position_string $board_width $board_height w 0 d 0 1").substitute(locals())
