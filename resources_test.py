from Game import Game
import unittest

class TestCreateGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.user_ids = (13, 22)

    def test_create_game(self):
        result = self.game.read()
        self.assertEqual(result["initial_fen"], 'c/c/c/c/c/c/c/c,0,0,0 12,8,12,d,-4,T o/1110/1121/2/f')

    def test_join_game(self):
        self.game.join(self.user_ids[0])
        self.game.join(self.user_ids[1])
        # print('===', self.game.participants, "===")
        self.assertEqual(len(self.game.participants), 2)

if __name__ == '__main__':
    unittest.main()
