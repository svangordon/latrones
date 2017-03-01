import unittest

from Users import create_user

class TestUsersMethods(unittest.TestCase):

    create_user_test_string = """INSERT INTO {users_table} (username)
    SELECT * FROM (SELECT '{username}') AS tmp
    WHERE NOT EXISTS(
	   SELECT username FROM {users_table} WHERE username = '{username}'
   ) LIMIT 1;
   """.format(users_table="users", username='doggy')

    def test_create_user(self):
        self.assertEqual(create_user('doggy'), self.create_user_test_string)

if __name__ == '__main__':
    unittest.main()
