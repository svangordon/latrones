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

    def test_point_to_alg(self):
        board_width = 12
        board_height = 8
        test_tuples = [(43, 'a3'), (124, 'l8'), (62, 'f4'), (100, 'b7')]
        for test in test_tuples:
            self.assertEqual(game_logic.convert_point_to_alg(test[0], board_width, board_height), test[1])

    def test_invalid_point_to_alg(self):
        board_width = 12
        board_height = 8
        test_squares = [0, 4, 13, 56, 126, 133, 139]
        for test in test_squares:
            with self.assertRaises(ValueError):
                game_logic.convert_point_to_alg(test, board_width, board_height)

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
