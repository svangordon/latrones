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

if __name__ == '__main__':
    unittest.main()
