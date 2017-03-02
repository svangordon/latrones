import hug
import latr
import unittest
import falcon

class TestGetUserMethods(unittest.TestCase):

    def setUp(self):
        self.test_user_id = 13
        self.resp = hug.test.get(latr, 'user/{0}'.format(self.test_user_id))

    def test_status_code(self):
        self.assertEqual(self.resp.status, falcon.HTTP_200)

    def test_resp_data(self):
        self.assertEqual(self.resp.data, {"user_id": 13, "username": "doggy"})

    def test_bad_id(self):
        bad_id_resp = hug.test.get(latr, 'user/0')
        self.assertEqual(bad_id_resp.status, falcon.HTTP_404)

class TestCreateUser(unittest.TestCase):

    def setUp(self):
        self.test_username = "test_user"
        self.resp = hug.test.post(latr, 'user', {'username': self.test_username})

    def test_status_code(self):
        self.assertEqual(self.resp.status, falcon.HTTP_200)

    def test_resp_data(self):
        self.assertEqual(self.resp.data['username'], self.test_username)

    def test_duplicate_fail(self):
        add_duplicate_resp = hug.test.post(latr, 'user', {'username': self.test_username})
        self.assertEqual(add_duplicate_resp.status, falcon.HTTP_403)

    def tearDown(self):
        latr.delete_user_handler(self.resp.data['user_id'])

class TestDeleteUser(unittest.TestCase):
    def setUp(self):
        self.test_username = 'test_user'
        self.createResp = hug.test.post(latr, 'user', {'username': self.test_username})
        self.deleteResp = hug.test.delete(latr, 'user/{0}'.format(self.createResp.data["user_id"]))

    def test_status_code(self):
        self.assertEqual(self.deleteResp.status, falcon.HTTP_200)

    def test_user_gone(self):
        getResp = hug.test.get(latr, 'user/{0}'.format(self.createResp.data["user_id"]))
        self.assertEqual(getResp.status, falcon.HTTP_404)

class TestGetGame(unittest.TestCase):
    def setUp(self):
        self.test_game = 1
        self.getResp = hug.test.get(latr, 'game/{0}'.format(self.test_game))

    def test_status_code(self):
        self.assertEqual(self.getResp.status, falcon.HTTP_200)

    def test_height(self):
        self.assertEqual(self.getResp.data["board_height"], 8)

    def test_width(self):
        self.assertEqual(self.getResp.data["board_width"], 8)

class TestGetParticipant(unittest.TestCase):
    def setUp(self):
        self.participant_id = 1
        self.getResp = latr.get_participant(self.participant_id)
        self.expected = {"participant_id": 1, "user_id": 13, "game_id": 8}

    def test_resp(self):
        self.assertEqual(self.getResp, self.expected)
#
# class TestAddParticipant(unittest.TestCase):
#     def setUp(self):
#         self.user_id = 13
#         self.game_id = 8
#         self.addResp = latr.add_participant(self.user_id, self.game_id)
#
#     def test_participant_id(self):
#         self.assertEqual()

if __name__ == '__main__':
    unittest.main()
