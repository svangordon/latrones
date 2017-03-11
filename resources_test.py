from Resources import Game, User, Participant
import unittest
from db import cnx
from pprint import pprint

class TestCreateGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.user_ids = (13, 22)

    def test_create_game(self):
        result = self.game.read()
        self.assertEqual(result["initial_fen"], "oooooooooooo/c/c/c/c/c/c/OOOOOOOOOOOO,0,0,0 12,8,12,d,-4,T o/0111/2111/2/f")

    def test_join_game(self):
        self.game.join(self.user_ids[0])
        self.game.join(self.user_ids[1])
        self.assertEqual(len(self.game.participants), 2)
        self.game.make_move(13, "a1 a2")
        self.game.make_move(22, "k8 k7")
        self.assertEqual(self.game.moves[-1]["fen"], "1ooooooooooo/ob/c/c/c/c/aO1/OOOOOOOOOO1O,0,2,1 12,8,12,d,-4,T o/0111/2111/2/f")

    def tearDown(self):
        self.game.delete()

class TestCreateUser(unittest.TestCase):
    def setUp(self):
        self.username1 = "electric_wizard"

    def test_create_user(self):
        user = User()
        user.create({"username": "electric_wizard"})
        self.assertEqual(user.username, self.username1)

    def tearDown(self):
        user = User(self.username1)
        user.delete()

# class TestFlow(unittest.TestCase):
#     def setUp(self):
#         self.username1 = "electric_wizard"
#         self.username2 = "dopethrone"
#
#     def test_create_user(self):
#         user1 = User()
#         user1.create(self.username1)
#         user2 = User()
#         user2.create(self.username2)



if __name__ == '__main__':
    unittest.main()
