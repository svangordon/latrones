import unittest
from game_class import GameState
from pprint import pprint

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
    def test_determine_direction_2(self):
        """ should find eastward direction ok """
        test_vals = self.test_vals[3]
        self.assertEqual(self.game.square(test_vals[0]).determine_direction(test_vals[1]), test_vals[2])

class TestHandleMove(unittest.TestCase):
    def setUp(self):
        self.game = GameState("12/1o10/12/12/12/12/12/12,0,0,1 12,8,12,d,-4,T o/1101/1121/2/f")
        # self.game.gen.piece('o', 30)

    def test_fen(self):
        # for square in range(len(self.game.turn["board"])):
            # print(self.game.turn["board"][square].position, self.game.turn["board"][square].char)
        # raise ValueError(vars(self.game.square(30)))
        # self.game.handle_move("b2 c2")
        # "12/1o10/12/12/12/12/12/12,0,0,1 12,8,12,d,-4,T o/1101/1121/2/f"
        self.game.serialize_fen_string()
        # raise ValueError(self.game.square())
        self.assertEqual("12/1o10/12/12/12/12/12/12,0,0,1 12,8,12,d,-4,T o/1101/1121/2/f", self.game.fen_string)
        # self.assertEqual("12/2o9/12/12/12/12/12/12,0,0,1 12,8,12,d,-4,T o/1101/1121/2/f", self.game.fen_string)
        # self.assertTrue(self.game.serialize_fen_string())

if __name__ == '__main__':
    unittest.main()
