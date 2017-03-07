import unittest
import game_logic
import fen
import game_logic

class TestSquareConversion(unittest.TestCase):
    """ make sure the game can convert algebraic coordinates to/from indices """
    def setUp(self):
        self.game = fen.deserialize_fen_string(fen.create_fen(12,8))

    def test_convert_algebraic_to_point(self):
        square = 'e4'
        # board_width = 12
        board_height = 8
        resp = game_logic.convert_alg_to_point(self.game, square)
        expected_resp = 61
        self.assertEqual(expected_resp, resp)
    #
    # def test_side_edge_alg_to_point(self):
    #     square = 'a6'
    #     board_width = 12
    #     board_height = 8
    #     resp = game_logic.convert_alg_to_point(square, board_width, board_height)
    #     expected_resp = 85
    #     self.assertEqual(expected_resp, resp)
    #
    # def test_bottom_edge_alg_to_point(self):
    #     square = 'f8'
    #     board_width = 12
    #     board_height = 8
    #     resp = game_logic.convert_alg_to_point(square, board_width, board_height)
    #     expected_resp = 118
    #     self.assertEqual(expected_resp, resp)
    #
    # def test_invalid_col(self):
    #     square = 'm8'
    #     board_width = 12
    #     board_height = 8
    #     with self.assertRaises(ValueError):
    #         game_logic.convert_alg_to_point(square, board_width, board_height)
    #     # expected_resp = None # maybe should raise?
    #     # self.assertEqual(expected_resp, resp)
    #
    # def test_invalid_row(self):
    #     square = 'b9'
    #     board_width = 12
    #     board_height = 8
    #     with self.assertRaises(ValueError):
    #         game_logic.convert_alg_to_point(square, board_width, board_height)
    #
    # def test_point_to_alg(self):
    #     board_width = 12
    #     board_height = 8
    #     test_tuples = [(43, 'a3'), (124, 'l8'), (62, 'f4'), (100, 'b7')]
    #     for test in test_tuples:
    #         self.assertEqual(game_logic.convert_point_to_alg(test[0], board_width, board_height), test[1])
    #
    # def test_invalid_point_to_alg(self):
    #     board_width = 12
    #     board_height = 8
    #     test_squares = [0, 4, 13, 56, 126, 133, 139]
    #     for test in test_squares:
    #         with self.assertRaises(ValueError):
    #             game_logic.convert_point_to_alg(test, board_width, board_height)

# class TestMoveValidation(unittest.TestCase):
#     # def setUp(self):
#
#     def test_simple_moves(self):
#         white_fen = '12/12/12/12/12/12/4w7/12 12 8 w 0 0 1'
#         white_dict = fen.deserialize_fen_string(white_fen)
#         white_test_dest = [('d6', True), ('c7', True), ('e7', True), ('d8', False), ('g6', False), ('a1', False)]
#         black_fen = '12/12/12/12/12/12/4b7/12 12 8 b 0 0 1'
#         black_dict = fen.deserialize_fen_string(black_fen)
#         black_test_dest = [('d6', False), ('c7', True), ('e7', True), ('d8', True), ('g6', False), ('a1', False)]
#         piece_start = 'd7'
#         for test in white_test_dest:
#             self.assertEqual(game_logic.validate_move(white_dict, piece_start, test[0]), test[1])
#         for test in black_test_dest:
#             self.assertEqual(game_logic.validate_move(black_dict, piece_start, test[0]), test[1])
#
#     def test_no_clip_moves(self):
#         """ Test that can't clip enemy piece """
#         white_fen = '12/1b10/12/12/12/4b7/3bwb6/4b7 12 8 w 0 0 1'
#         white_dict = fen.deserialize_fen_string(self.white_fen)
#         black_fen = '12/1w10/12/12/12/4w7/3wbw6/4w7 12 8 b 0 0 1'
#         black_dict = fen.deserialize_fen_string(self.black_fen)
#         move_squares = ['c7', 'd6', 'd8', 'e7']
#         start_move = 'd7'
#         for square in move_squares:
#             self.assertFalse(game_logic.validate_move(white_dict, start_move, square))
#             self.assertFalse(game_logic.validate_move(black_dict, start_move, square))
#
#     def test_move_own_only(self):
#         """ Test that can't move opponent's pieces """
#         white_fen = '12/12/12/12/12/12/4w7/12 12 8 b 0 0 1'
#         black_fen = '12/12/12/12/12/12/4w7/12 12 8 w 0 0 1'
#         white_dict = fen.deserialize_fen_string(white_fen)
#         black_dict = fen.deserialize_fen_string(black_fen)
#         start_move = 'd7'
#         end_move = 'c7'
#         self.assertFalse(game_logic.validate_move(white_dict, start_move, end_move))
#         self.assertFalse(game_logic.validate_move(black_dict, start_move, end_move))

class TestIsMoveBackwards(unittest.TestCase):
    def setUp(self):
        self.fn = game_logic.is_backwards
        # self.game = fen.deserialize_fen_string(fen.create_fen(8,12))
# (move_start, move_end, active_player, board_width)
    def test_values(self):
        game = fen.deserialize_fen_string(fen.create_fen(12, 8))
        tests = [(False, (61, 75)), (False, (61, 62)), (False, (61, 60)), (True, (61, 47))]
        for test in tests:
            self.assertEqual(test[0], self.fn(game, *test[1]))

# class TestValidateJump(unittest.TestCase):
#     def setUp(self):
#         self.fn = game_logic.validate_jump
#         self.valid_fen = "12/12/3w8/3wb7/3w8/3B8/12/12 12 8 b 0 0 1"
#         self.valid_dict = fen.deserialize_fen_string(self.valid_fen)
#         self.invalid_fen = "12/12/3b8/3w8/3w8/3b8/12/12 12 8 b 0 0 1"
#         self.invalid_dict = fen.deserialize_fen_string(self.invalid_fen)
#
#     def test_valid_jumps(self):
#         start = 60
#         jump_coords = [(60, 61, 62), (60, 46, 32), (60, 74, 88)]
#         jump_coords = [(60, 61, 62)]
#         for coord in jump_coords:
#             self.assertTrue(self.fn(*coord, self.valid_dict))
#
#     def test_valid_setup(self):
#         self.assertEqual(self.valid_dict["board"][60]["owner"], 0)
#
#     def test_invalid_jumps(self):
#         # jump_coords = [(60, 61, 62), (60, 46, 32), (60, 74, 88)]
#         jump_coords = [(60, 61, 62)]
#         for coord in jump_coords:
#             self.assertFalse(self.fn(*coord, self.invalid_dict))

class TestCheckAdjacent(unittest.TestCase):
    def setUp(self):
        fen_string = '12/12/12/12/12/12/12/12 12 8 w 0 0 1'
        self.game = fen.deserialize_fen_string(fen_string)
        self.central_square = 62
        self.adjacent_squares = [48, 61, 63, 76]
        self.fn = game_logic.check_adjacent
        self.non_adjacent_squares = [[47, 49, 75, 77], [48, 15, 93, 83]]

    def test_single_square(self):
        for square in self.adjacent_squares:
            self.assertTrue(self.fn(self.game, self.central_square, square))

    def test_multiple_squares(self):
        self.assertTrue(self.fn(self.game, self.central_square, *self.adjacent_squares))

    def test_non_adjacent_squares(self):
        for squares in self.non_adjacent_squares:
            self.assertFalse(self.fn(self.game, self.central_square, *squares))

    def test_square_count(self):
        with self.assertRaises(ValueError):
            self.fn(self.game, 69, *[48, 61, 63, 76, 69])

    def test_type_validation(self):
        with self.assertRaises(TypeError):
            self.fn(self.game, 69, [1, 2, 3])

class TestCheckAttr(unittest.TestCase):
    def setUp(self):
        self.fen_string = "wWbB8/12/3w8/3wb7/3w8/3B8/12/12 12 8 b 0 0 1"
        self.game = fen.deserialize_fen_string(self.fen_string)
        self.fn = game_logic.check_attr

    def test_check_check(self):
        checked = [16, 18]
        not_checked = [14, 15, 19]
        self.assertTrue(self.fn(self.game, 'checked', True, *checked))
        self.assertFalse(self.fn(self.game, 'checked', False, checked))
        self.assertFalse(self.fn(self.game, 'checked', True, *not_checked))
        self.assertTrue(self.fn(self.game, 'checked', False, not_checked))
        self.assertFalse(self.fn(self.game, 'checked', False, *checked, *not_checked))
        self.assertFalse(self.fn(self.game, 'checked', True, *checked, *not_checked))

    def test_check_occupied(self):
        occupied = [15, 16, 17, 18]
        not_occupied = [14, 19]
        self.assertTrue(self.fn(self.game, "occupied", True, occupied))
        self.assertFalse(self.fn(self.game, "occupied", False, *occupied))
        self.assertFalse(self.fn(self.game, "occupied", True, not_occupied))
        self.assertTrue(self.fn(self.game, "occupied", False, *not_occupied))
        self.assertFalse(self.fn(self.game, "occupied", True, *occupied, *not_occupied))
        self.assertFalse(self.fn(self.game, "occupied", False, *occupied, *not_occupied))

    def test_check_valid(self):
        valid = [15, 16, 17, 18, 19, 33, 47, 48]
        not_valid = [0, 13, 126, 139, 6, 56, 55]
        self.assertTrue(self.fn(self.game, "valid", True, valid))
        self.assertFalse(self.fn(self.game, "valid", False, *valid))
        self.assertTrue(self.fn(self.game, "valid", False, not_valid))
        self.assertFalse(self.fn(self.game, "valid", True, *not_valid))
        self.assertFalse(self.fn(self.game, "valid", True, *valid, *not_valid))
        self.assertFalse(self.fn(self.game, "valid", False, *valid, *not_valid))

    def test_check_owner(self):
        owner_white = [15, 16]
        owner_black = [17, 18]
        owner_none = [14, 19]
        self.assertTrue(self.fn(self.game, "owner", 0, owner_white))
        self.assertTrue(self.fn(self.game, "owner", 1, owner_black))
        self.assertTrue(self.fn(self.game, "owner", -1, owner_none))
        self.assertFalse(self.fn(self.game, "owner", 0, *owner_white, *owner_black))
        self.assertFalse(self.fn(self.game, "owner", 1, *owner_white, *owner_black))
        self.assertFalse(self.fn(self.game, "owner", -1, *owner_none, *owner_black))

class TestCheckPieceArrival(unittest.TestCase):
    def setUp(self):
        self.fen_string = "wWbB8/12/3w8/3wb7/3w8/3B8/12/12 12 8 b 0 0 1"
        self.game = fen.deserialize_fen_string(self.fen_string)
        self.game["rules"] = {}
        self.fn = game_logic.check_piece_arrival

    def test_with_custod(self):
        self.game["rules"]["displacement_capture"] = True
        valid_move_pairs = [(15, 18), (15, 29), (17, 16), (17, 31)]
        for move in valid_move_pairs:
            self.assertTrue(self.fn(self.game, *move))

    def test_invalid_move_pairs(self):
        self.game["rules"]["displacement_capture"] = False
        invalid_move_pairs = [(15, 18), (15, 16), (17, 16), (17, 18)]
        for move in invalid_move_pairs:
            self.assertFalse(self.fn(self.game, *move))

class TestValidateMove(unittest.TestCase):
    def setUp(self):
        self.fn = game_logic.validate_move

    def test_simple_moves(self):
        game = fen.deserialize_fen_string("wWbB8/12/3w8/4b7/3w8/3B8/12/12 12 8 b 0 0 1")
        game["rules"] = {"allow_backwards": True}
        start = 46
        valid = [32, 60, 45, 47]
        for move in valid:
            self.assertTrue(self.fn(game, start, move))

class TestValidateJump(unittest.TestCase):
    def setUp(self):
        self.fn = game_logic.validate_jump

    def test_simple_jump(self):
        game = fen.deserialize_fen_string("wWbB8/12/3w8/4b7/12/3B8/12/12 12 8 b 0 0 1")
        game["rules"] = {"allow_backwards": True, "allow_jump_enemy_backwards": True}
        start = 46
        self.assertTrue(self.fn(game, 46, 74))

class TestIsChecking(unittest.TestCase):
    def setUp(self):
        self.is_checking = game_logic.is_checking

    def test_simple(self):
        game = fen.deserialize_fen_string("12/12/3wbw6/12/12/12/12/12 12 8 b 0 0 1")
        expected = [47]
        result = self.is_checking(game, 46, True)
        self.assertEqual(expected, result)

class TestIsSandwiched(unittest.TestCase):
    def setUp(self):
        self.fn = game_logic.is_sandwiched

    def test_is_sandwiched(self):
        game = fen.deserialize_fen_string("12/12/3wBw6/12/12/4w7/3wbw6/4w7 12 8 b 0 0 1")
        expected = [[(46, 48)], [(102, 104), (89, 117)]]
        cnt = 0
        for i in range(len(game["board"])):
            if game["board"][i]["owner"] == 1:
                self.assertEqual(self.fn(game, i), expected[cnt])
                cnt += 1

class TestModifyGame(unittest.TestCase):
    def setUp(self):
        self.modify_game = game_logic.modify_game

    def execute_test(self, move_start, move_end, fen_start, fen_end):
        game = fen.deserialize_fen_string("12/12/3wBw6/12/12/4w7/3wbw6/4w7 12 8 b 0 0 1")
        self.modify_game(game, move_start, move_end)
        return (fen_end, fen.serialize_fen_string(game))

    def test_simple_move(self):
        game = fen.deserialize_fen_string("12/12/3wBw6/12/12/4w7/3wbw6/4w7 12 8 b 0 0 1")
        expected = "12/3w8/4bw6/12/12/4w7/3wbw6/4w7 12 8 b 0 0 1"
        self.modify_game(game, 46, 32)
        self.assertEqual(expected, fen.serialize_fen_string(game))

    def test_execute_test(self):
        var = (46, 32, "12/12/3wBw6/12/12/4w7/3wbw6/4w7 12 8 b 0 0 1", "12/3w8/4bw6/12/12/4w7/3wbw6/4w7 12 8 b 0 0 1")
        self.assertEqual(*self.execute_test(*var))
if __name__ == '__main__':
    unittest.main()
