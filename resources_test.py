from Game import Game
import unittest
from db import cnx

class TestCreateGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.user_ids = (13, 22)

    def test_create_game(self):
        result = self.game.read()
        self.assertEqual(result["initial_fen"], "oooooooooooo/c/c/c/c/c/c/OOOOOOOOOOOO,0,0,0 12,8,12,d,-4,T o/1110/1121/2/f")

    def test_join_game(self):
        self.game.join(self.user_ids[0])
        self.game.join(self.user_ids[1])
        # print('===', self.game.participants, "===")
        self.assertEqual(len(self.game.participants), 2)
        self.game.make_move(13, "a1 a2")
        self.game.make_move(22, "k8 k7")
        self.assertEqual(self.game.read["fen"], "1ooooooooooo/ob/c/c/c/c/aO1/OOOOOOOOOO1O,0,0,0 12,8,12,d,-4,T o/1110/1121/2/f")

    # def tearDown(self):
        # cur = cnx.cursor()
        # cur.execute("""DELETE FROM game WHERE game_id = {0}""".format(self.game.resource_id))
        # cur.execute("DELETE FROM ")

if __name__ == '__main__':
    unittest.main()
