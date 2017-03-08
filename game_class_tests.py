import unittest
from game_class import GameState

class TestRules(unittest.TestCase):

    def setUp(self):
        self.game = GameState("standard", True)

    def test_basic(self):
        self.game.make_move("a1 a2")

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
