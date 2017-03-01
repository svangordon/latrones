import constants
from constants import sql_templates


def create_user(username, email="email@address.com"):
    """ Return an SQL query string to add a user to DB if not exists """

    sql = sql_templates["create_user"].format(users_table=constants.db["users"], username=username)

    return sql

def get_user(user_id):
    """ Return SQL string to read user by Id """

    sql = sql_templates["get_user"].format(users_table=constants.db['users'], user_id=user_id)

    return sql
