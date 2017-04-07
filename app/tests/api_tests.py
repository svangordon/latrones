# import hug
# import latr
import unittest
# import falcon
import datetime



# class TestGetUserMethods(unittest.TestCase):
#
#     def setUp(self):
#         self.test_user_id = 13
#         self.resp = hug.test.get(latr, 'user/{0}'.format(self.test_user_id))
#
#     def test_status_code(self):
#         self.assertEqual(self.resp.status, falcon.HTTP_200)
#
#     def test_resp_data(self):
#         self.assertEqual(self.resp.data, {"user_id": 13, "username": "doggy"})
#
#     def test_bad_id(self):
#         bad_id_resp = hug.test.get(latr, 'user/0')
#         self.assertEqual(bad_id_resp.status, falcon.HTTP_404)
#
# class TestCreateUser(unittest.TestCase):
#
#     def setUp(self):
#         self.test_username = "test_user"
#         self.resp = hug.test.post(latr, 'user', {'username': self.test_username})
#
#     def test_status_code(self):
#         self.assertEqual(self.resp.status, falcon.HTTP_200)
#
#     def test_resp_data(self):
#         self.assertEqual(self.resp.data['username'], self.test_username)
#
#     def test_duplicate_fail(self):
#         add_duplicate_resp = hug.test.post(latr, 'user', {'username': self.test_username})
#         self.assertEqual(add_duplicate_resp.status, falcon.HTTP_403)
#
#     def tearDown(self):
#         latr.delete_user_handler(self.resp.data['user_id'])
#
# class TestDeleteUser(unittest.TestCase):
#     def setUp(self):
#         self.test_username = 'test_user'
#         self.createResp = hug.test.post(latr, 'user', {'username': self.test_username})
#         self.deleteResp = hug.test.delete(latr, 'user/{0}'.format(self.createResp.data["user_id"]))
#
#     def test_status_code(self):
#         self.assertEqual(self.deleteResp.status, falcon.HTTP_200)
#
#     def test_user_gone(self):
#         getResp = hug.test.get(latr, 'user/{0}'.format(self.createResp.data["user_id"]))
#         self.assertEqual(getResp.status, falcon.HTTP_404)
#
# class TestGetGame(unittest.TestCase):
#     def setUp(self):
#         self.expected = {
#             "board_height": 8,
#             "board_width": 8,
#             "game_id": 1,
#             "start_time": datetime.datetime(2017, 3, 1, 16, 55, 57)
#         }
#         self.test_game = 1
#         self.getResp = hug.test.get(latr, 'game/{0}'.format(self.test_game))
#
#     def test_http_exists(self):
#         get_resp = hug.test.get(latr, 'game/{0}'.format(self.test_game))
#         self.assertIsNotNone(get_resp)
#
#     def test_http_status_code(self):
#         get_resp = hug.test.get(latr, 'game/{0}'.format(self.test_game))
#         self.assertEqual(get_resp.status, falcon.HTTP_200)
#
#     def test_http_value(self):
#         get_resp = hug.test.get(latr, 'game/{0}'.format(self.test_game))
#         self.assertEqual(get_resp.data, self.expected)
#
#     def test_local_exists(self):
#         get_resp = latr.get_game_handler(self.test_game)
#         self.assertIsNotNone(get_resp)
#
#     def test_http_value(self):
#         get_resp = get_resp = latr.get_game_handler(self.test_game)
#         self.assertEqual(get_resp, self.expected)
#
# class TestGetParticipant(unittest.TestCase):
#     def setUp(self):
#         self.not_found_id = 0
#         self.participant_id = 1
#         self.getResp = latr.get_participant(self.participant_id)
#         self.expected = {"participant_id": 1, "user_id": 13, "game_id": 8}
#
#     def test_resp(self):
#         getResp = latr.get_participant(self.participant_id)
#         self.assertEqual(self.getResp, self.expected)
#
#     def test_not_found(self):
#         getResp = latr.get_participant(self.not_found_id)
#         self.assertIsNone(getResp)
#
# class TestDeleteParticipant(unittest.TestCase):
#     def test_participant_gone(self):
#         participant = latr.add_participant(13, 1)
#         latr.delete_participant(participant)
#         getResp = latr.get_participant(participant)
#         self.assertIsNone(getResp)
#
# class TestAddParticipant(unittest.TestCase):
#     def setUp(self):
#         self.user_id = 13
#         self.game_id = 8
#         self.add_resp = latr.add_participant(self.user_id, self.game_id)
#         self.expected = (self.user_id, self.game_id)
#         self.returned = ()
#
#     def test_participant_exists(self):
#         self.assertIsNotNone(self.add_resp)
#
#     def test_fk_ids(self):
#         added = latr.get_participant(self.add_resp)
#         returned = (added["user_id"], added["game_id"])
#         self.assertEqual(returned, self.expected)
#
#     def tearDown(self):
#         latr.delete_participant(self.add_resp)
#
# class TestAddGame(unittest.TestCase):
#     def setUp(self):
#         self.user_id = 13
#         self.add_resp = latr.add_game(self.user_id)
#
#     def test_exists(self):
#         self.assertIsNotNone(latr.get_game_handler(self.add_resp))
#
#     def test_values(self):
#         self.assertEqual
#
#     def tearDown(self):
#         latr.delete_game(self.add_resp)
#
# class TestDeleteGame(unittest.TestCase):
#     def test_participant_gone(self):
#         game = latr.add_game(13)
#         latr.delete_game(game)
#         getResp = latr.get_game_handler(game)
#         self.assertIsNone(getResp)
#
# class TestGetParticipantByUser(unittest.TestCase):
#     """ This is probably going to wind up abandonded. """
#     def setUp(self):
#         self.user_id = 22
#         self.expected = ((10, 22, 1), (11, 22, 8))
#
#     def test_values(self):
#         self.assertEqual(latr.get_participant_by_user(self.user_id), self.expected)
#
# class TestGetGameByUser(unittest.TestCase):
#     def setUp(self):
#         self.user_id = 22
#         self.expected = ((1, datetime.datetime(2017, 3, 1, 16, 55, 57), 8, 8), (8, datetime.datetime(2017, 3, 1, 17, 17, 2), 8, 8))
#
#     def test_values(self):
#         self.assertEqual(latr.get_games_by_user(self.user_id), self.expected)
#
# class TestMoveMethods(unittest.TestCase):
#     def setUp(self):
#         self.move_dict = {
#             "game_id": 1,
#             "half_move_clock": 1,
#             "notation": "a1 a2",
#             "position": "8/w7/8/8/8/8/8/8/8/8/8/8 8 12 w 0 0 1"
#         }
#
#     def test_add_move(self):
#         fn = latr.add_move
#         added = fn(self.move_dict)
#         expected = (added, 1, 1, 'a1 a2', '8/w7/8/8/8/8/8/8/8/8/8/8 8 12 w 0 0 1')
#         self.assertEqual(expected, latr.get_move(added))
#         latr.delete_move(added)
#         self.assertIsNone(latr.get_move(added))
#         # self.assertEqual(fn(self.move_dict), 'INSERT INTO move (game_id, half_move_clock, notation, position) VALUES (1, 1, "a1 a2", "8/w7/8/8/8/8/8/8/8/8/8/8 8 12 w 0 0 1")')

if __name__ == '__main__':
    unittest.main()
