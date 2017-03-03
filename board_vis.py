"""Just to make it easier to visualize board for tests, etc"""
from string import ascii_lowercase
# 1 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11,
# 2 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
# 3 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
# 4 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
# 5 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
# 6 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
# 7 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
# 8 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95
#   a   b   c   d   e   f   g   h   i   j   k   l
#
# 12 x 8
#    000, 001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013,
# 1  014, 015, 016, 017, 018, 019, 020, 021, 022, 023, 024, 025, 026, 027,
# 2  028, 029, 030, 031, 032, 033, 034, 035, 036, 037, 038, 039, 040, 041,
# 3  042, 043, 044, 045, 046, 047, 048, 049, 050, 051, 052, 053, 054, 055,
# 4  056, 057, 058, 059, 060, 061, 062, 063, 064, 065, 066, 067, 068, 069,
# 5  070, 071, 072, 073, 074, 075, 076, 077, 078, 079, 080, 081, 082, 083,
# 6  084, 085, 086, 087, 088, 089, 090, 091, 092, 093, 094, 095, 096, 097,
# 7  098, 099, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
# 8  112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125,
#    126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]
#         a    b    c    d    e    f    g    h    i    j    k    l

def create_board_vis(board_width, board_height):
    board_width += 2
    board_height += 2
    output = ''
    if board_width * board_height > 99:
        pad_len = 3
    else:
        pad_len = 2
    row_count = 0
    col_count = 0
    for i in range(board_width * board_height):
        if i % board_width == 0:
            if row_count != 0:
                output += '\n'
            if 0 < row_count <= board_height-2:
                output += str(row_count).ljust(pad_len)
            else:
                output += ' ' * pad_len
            row_count += 1
        output += str(i).zfill(pad_len)
        output += ', '
    output += '\n'
    output += ' ' * (3 + pad_len + 2)
    for i in range(board_width - 2):
        output += ascii_lowercase[i]
        output += ' ' * (pad_len + 1)
    print(output)

create_board_vis(8, 12)
