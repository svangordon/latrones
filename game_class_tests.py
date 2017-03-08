import unittest
from game_class import GameState

class TestRules(unittest.TestCase):

    def setUp(self):
        self.game = GameState("standard", True)
        self.game.gen.piece('o', 15)
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



    # def test_basic(self):
        # self.game.handle_move(15, 16)

    # def test_deserialize_rules(self):
    #     self.game.deserialize_rules("d,-4,T")
    #     self.assertEqual(self.game.rules["capture_method"], "displacement")
    #     self.assertEqual(self.game.rules["win_condition"], -4)
    #     self.assertTrue(self.game.rules["trapping"])
    #
    # def test_serialize_rules(self):
    #     self.game.deserialize_rules("d,-4,T")
    #     self.assertEqual("d,-4,T", self.game.serialize_rules())
#
# class TestPieces(unittest.TestCase):
#     def setUp(self):
#         self.game = GameState("standard", True)
#
#     def test_deserialize(self):
#         self.game.deserialize_pieces("o/1101/1121/2222/2/f")
#         self.assertEqual(self.game.serialize_pieces(), "o/1101/1121/2222/2/f")

if __name__ == '__main__':
    unittest.main()
