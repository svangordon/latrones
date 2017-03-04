"""
fn needed:
    -- check_adjacent(central_square, *args)
    -- check_valid(*args)
    -- check_backwards
    -- check_occupy_square(start, end, game_state)
        -- does the various (check if it's occupied, and if it is, check if it's
        in check, and there's displacement capture, etc)
    -- check_sandwich (find better name)
    -- check_is_occupied
"""

def check_adjacent(game, central_square, *squares):
    """ Returns if all args are adjacent to central_square """
    row_width = game["board_width"] + 2
    if len(squares) > 4:
        return False
    for square in squares:
        if square not in [central_square + 1, central_square - 1,
        central_square + row_width, central_square - row_width]:
            return False
    return True
