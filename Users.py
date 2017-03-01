import constants

def create_user(username, email="email@address.com"):
    """ Return an SQL query string to add a user to DB if not exists """

    sql = """INSERT INTO {users_table} (username)
    SELECT * FROM (SELECT '{username}') AS tmp
    WHERE NOT EXISTS(
	   SELECT username FROM {users_table} WHERE username = '{username}'
   ) LIMIT 1;
   """.format(users_table=constants.db["users"], username=username)

    return sql

def get_user(userid):
    """ Return SQL string to read user by Id """

    sql = """SELECT * FROM {users_table} WHERE user_id = {userid}
    """.format(users_table=constants.db['users'], userid=userid)

    return sql
