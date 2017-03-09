import unittest
from game_class import GameState
from pprint import pprint

class TestConvertChar(unittest.TestCase):
    def setUp(self):
        self.game = GameState("standard", True)
        self.vals = [(1, 1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), ('a', 10), ('b', 11), ('c', 12), ('d', 13), ('e', 14), ('f', 15)]

    def test_hex_to_dec(self):
        for val in self.vals:
            self.assertEqual(self.game.convert_char(val[0]), val[1])
    def test_dec_to_hex(self):
        for val in self.vals:
            self.assertEqual(self.game.convert_char(val[1]), val[0])
    def test_convert_string(self):
        """ should throw on trying to convert a piece """
        with self.assertRaises(ValueError):
            for char in "oOgGlL":
                self.game.convert_char(char)

class TestDetermineDirection(unittest.TestCase):

    def setUp(self):
        self.game = GameState("standard", True)
        self.game.gen.piece('o', 30)
        # Order: NEWS (so that if you reverse the string, you swap which is in what directions)
        self.test_vals = [(30,16,0), (30,31,1), (30,29,2), (30,44,3)]

    def test_determine_direction_n(self):
        """ should find eastward direction ok """
        test_vals = self.test_vals[0]
        self.assertEqual(self.game.square(test_vals[0]).determine_direction(test_vals[1]), test_vals[2])
    def test_determine_direction_e(self):
        """ should find eastward direction ok """
        test_vals = self.test_vals[1]
        self.assertEqual(self.game.square(test_vals[0]).determine_direction(test_vals[1]), test_vals[2])
    def test_determine_direction_s(self):
        """ should find eastward direction ok """
        test_vals = self.test_vals[2]
        self.assertEqual(self.game.square(test_vals[0]).determine_direction(test_vals[1]), test_vals[2])
    def test_determine_direction_w(self):
        """ should find eastward direction ok """
        test_vals = self.test_vals[3]
        self.assertEqual(self.game.square(test_vals[0]).determine_direction(test_vals[1]), test_vals[2])
    # def test_determine_direction_sw(self):
    #     """ """

class TestHandleMove(unittest.TestCase):
    def setUp(self):
        self.game = GameState("12/1o10/12/12/12/12/12/12,0,0,1 12,8,12,d,-4,T o/1101/1121/2/f")
        self.test_fens = [{
            "start": "12/1o10/12/12/12/12/12/12,0,0,1 12,8,12,d,-4,T o/1101/1121/2/f",
            "end": "12/2o9/12/12/12/12/12/12,0,0,1 12,8,12,d,-4,T o/1101/1121/2/f",
            "move": "b2 c2"
        }, {
            "start": "12/1o10/1o10/12/12/12/12/12,0,0,1 12,8,12,d,-4,T o/1101/1121/2/f",
            "end": "12/12/1o10/1o10/12/12/12/12,0,0,1 12,8,12,d,-4,T o/1101/1121/2/f",
            "move": "b2 b4"
        }, {
            "start": "12/1o10/12/12/12/12/12/12,0,0,1 12,8,12,d,-4,T o/1101/1121/2/f",
            "end": None,
            "move": "b2 e8"
        }]

    def test_simple_move(self):
        test_fens = self.test_fens[0]
        game = GameState(test_fens["start"])
        game.handle_move(test_fens["move"])
        game.serialize_fen_string()
        self.assertEqual(test_fens["end"], game.fen_string)

    def test_simple_jump(self):
        test_fens = self.test_fens[1]
        game = GameState(test_fens["start"])
        game.handle_move(test_fens["move"])
        game.serialize_fen_string()
        self.assertEqual(test_fens["end"], game.fen_string)

    # def test_invalid_move(self):
    #     test_fens = self.test_fens[1]
    #     game = GameState(test_fens["start"])
    #     # with self.assertRaises(ValueError):
    #     game.handle_move(test_fens["move"])

    # def test_all(self):
    #     for test in self.test_fens:
    #         game = GameState(test["start"])
    #         game.handle_move(test["move"])
    #         game.serialize_fen_string()
    #         self.assertEqual(game.fen_string, test["end"])

if __name__ == '__main__':
    unittest.main()
