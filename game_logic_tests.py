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

class TestMoveValidation(unittest.TestClass):
    def setUp(self):

    def test_simple_moves(self):
        white_fen = '12/12/12/12/12/12/4w7/12 12 8 w 0 0 1'
        white_dict = fen.deserialize_fen_string(self.one_piece_fen)
        white_test_dest = [('d6', True), ('c7', True), ('e7', True), ('d8', False), ('g6', False), ('a1', False)]
        black_fen = '12/12/12/12/12/12/4b7/12 12 8 b 0 0 1'
        black_dict = fen.deserialize_fen_string(self.one_piece_fen)
        black_test_dest = [('d6', False), ('c7', True), ('e7', True), ('d8', True), ('g6', False), ('a1', False)]
        piece_start = 'd7'
        for test in white_test_dest:
            self.assertEqual(game_logic.validate_move(white_game_dict, piece_start, test[0]), test[1])
        for test in black_test_dest:
            self.assertEqual(game_logic.validate_move(black_game_dict, piece_start, test[0]), test[1])

    def test_no_clip_moves(self):
        """ Test that can't clip enemy piece """
        white_fen = '12/1b10/12/12/12/4b7/3bwb6/4b7 12 8 w 0 0 1'
        white_dict = fen.deserialize_fen_string(self.white_fen)
        black_fen = '12/1w10/12/12/12/4w7/3wbw6/4w7 12 8 b 0 0 1'
        black_dict = fen.deserialize_fen_string(self.black_fen)
        move_squares = ['c7', 'd6', 'd8', 'e7']
        start_move = 'd7'
        for square in move_squares:
            self.assertFalse(game_logic.validate_move(white_dict, start_move, square))
            self.assertFalse(game_logic.validate_move(black_dict, start_move, square))

    def test_move_own_only(self):
        """ Test that can't move opponent's pieces """
        white_fen = '12/12/12/12/12/12/4w7/12 12 8 b 0 0 1'
        black_fen = '12/12/12/12/12/12/4w7/12 12 8 w 0 0 1'
        white_dict = fen.deserialize_fen_string(white_fen)
        black_dict = fen.deserialize_fen_string(black_fen)
        start_move = 'd7'
        end_move = 'c7'
        self.assertFalse(game_logic.validate_move(white_dict, start_move, end_move))
        self.assertFalse(game_logic.validate_move(black_dict, start_move, end_move))

if __name__ == '__main__':
    unittest.main()
