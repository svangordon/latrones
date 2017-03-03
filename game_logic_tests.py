import unittest
import game_logic
import fen
import game_logic

class TestSquareConversion(unittest.TestCase):
    """ make sure the game can convert algebraic coordinates to/from indices """
    # def setUp(self):

    def test_convert_algebraic_to_point(self):
        square = 'e4'
        board_width = 12
        board_height = 8
        resp = game_logic.convert_alg_to_point(square, board_width, board_height)
        expected_resp = 61
        self.assertEqual(expected_resp, resp)

    def test_side_edge_alg_to_point(self):
        square = 'a6'
        board_width = 12
        board_height = 8
        resp = game_logic.convert_alg_to_point(square, board_width, board_height)
        expected_resp = 85
        self.assertEqual(expected_resp, resp)

    def test_bottom_edge_alg_to_point(self):
        square = 'f8'
        board_width = 12
        board_height = 8
        resp = game_logic.convert_alg_to_point(square, board_width, board_height)
        expected_resp = 118
        self.assertEqual(expected_resp, resp)

    def test_invalid_col(self):
        square = 'm8'
        board_width = 12
        board_height = 8
        with self.assertRaises(ValueError):
            game_logic.convert_alg_to_point(square, board_width, board_height)
        # expected_resp = None # maybe should raise?
        # self.assertEqual(expected_resp, resp)

    def test_invalid_row(self):
        square = 'b9'
        board_width = 12
        board_height = 8
        with self.assertRaises(ValueError):
            game_logic.convert_alg_to_point(square, board_width, board_height)
        # resp = game_logic.convert_alg_to_point(square, board_width, board_height)
        # expected_resp = None # maybe should raise?
        # self.assertEqual(expected_resp, resp)

# class TestMoveValidation(unittest.TestClass):
#     def setUp(self):
#         self.one_piece_fen = '12/12/12/12/12/12/4w7/12 12 8 w 0 0 1'
#         self.one_piece_dict = fen.deserialize_fen_string(self.one_piece_fen)
#
#     def test_white_move_forward(self):
#         move =
#         validation_resp = game

if __name__ == '__main__':
    unittest.main()
