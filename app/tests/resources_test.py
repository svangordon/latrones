from Resources import Game, User, Participant
import unittest
from db import cnx
from pprint import pprint

# class TestCreateGame(unittest.TestCase):
#       """ These tests are out of date, and will fail. """
#     def setUp(self):
#         self.game = Game()
#         self.user_ids = (13, 22)
#
#     def test_create_game(self):
#         result = self.game.read()
#         self.assertEqual(result["initial_fen"], "oooooooooooo/c/c/c/c/c/c/OOOOOOOOOOOO,0,0,0 12,8,12,d,-4,T o/0111/2111/2/f")
#
#     def test_join_game(self):
#         self.game.join(self.user_ids[0])
#         self.game.join(self.user_ids[1])
#         self.assertEqual(len(self.game.participants), 2)
#         self.game.make_move(13, "a1 a2")
#         self.game.make_move(22, "k8 k7")
#         self.assertEqual(self.game.moves[-1]["fen"], "1ooooooooooo/ob/c/c/c/c/aO1/OOOOOOOOOO1O,0,2,1 12,8,12,d,-4,T o/0111/2111/2/f")
#
#     def tearDown(self):
#         self.game.delete()

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

class TestUser(unittest.TestCase):
    def setUp(self):
        self.users = {"electric_wizard": User(), "dopethrone": User()}
        [User.clear(username) for username in self.users.keys()]
        for username, user in self.users.items():
            user.create({"username": username})

    def test_create_user(self):
        for username, user in self.users.items():
            self.assertEqual(user.username, username)

    def tearDown(self):
        for user in self.users.values():
            user.delete()

class TestGame(unittest.TestCase):
    def setUp(self):
        self.users = {"electric_wizard": User(), "dopethrone": User()}
        [User.clear(username) for username in self.users.keys()]
        for username, user in self.users.items():
            user.create({"username": username})

    def test_join_game(self):
        # users = self.users.values()
        game = Game()
        [user.join(game) for user in self.users.values()]
        self.assertEqual(len(game.participants), 2)
        self.assertEqual([user.resource_id for user in self.users.values()].sort(), [participant.user_id for participant in game.participants].sort())
        [user.leave(game) for user in self.users.values()]
        # self.assertEqual(game.participants, [])
        game.delete()
    def test_leave_game(self):
        game = Game()
        [user.join(game) for user in self.users.values()]
        [user.leave(game) for user in self.users.values()]
        self.assertEqual(game.participants, [])
        game.delete()
    def test_game_status(self):
        game = Game()
        [user.join(game) for user in self.users.values()]
        self.assertEqual(len(game.participants), 2)
        self.assertEqual(game.game_status, 1)
        game.delete()
    def test_make_move(self):
        game = Game()
        [user.join(game) for user in self.users.values()]
        for participant in game.participants:
            if participant.color == 0:
                game.make_move(User(participant.user_id), "a1 a2")
        for participant in game.participants:
            if participant.color == 1:
                game.make_move(User(participant.user_id), "k8 k7")
        self.assertEqual(game.fen, "1ooooooooooo/ob/c/c/c/c/aO1/OOOOOOOOOO1O,0,2,1 12,8,12,d,-4,T o/0111/2111/2/f")

    def tearDown(self):
        [user.delete() for user in self.users.values()]

if __name__ == '__main__':
    unittest.main()
