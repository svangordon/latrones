
import MySQLdb
import hug

import constants
from constants import sql_templates
from Users import create_user
from Users import get_user

cnx = MySQLdb.connect(host="localhost", user="igoinu", passwd="password", db="latr")

def db_wrapper(script, resp_flag):
    """ simple wrapper to execute MySQLdb queries and return one or more rows of results """
    cur = cnx.cursor()
    try:
        cur.execute(script)
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: %s" % str(e))
    try:
        if int(resp_flag) == 1:
            return cur.fetchone()
        elif int(resp_flag) > 0:
            return cur.fetchmany(int(resp_flag))
        return
    except TypeError:
        # resp_flag == None, and we're done
        return
    except ValueError:
        return cur.fetchmany()

@hug.get('/user/{user_id}')
def get_user_handler(user_id):
    cur = cnx.cursor()
    cur.execute(sql_templates["get_user"].format(user_id=user_id, users_table=constants.db["users"]))
    row=cur.fetchone()
    cur.close()
    return row

# print(db_wrapper(get_user(13)))
# print(get_user_handler(13))
@hug.post('/user')
def create_user_handler(username):
    cur = cnx.cursor()
    cur.execute(sql_templates["create_user"].format(username=username, users_table=constants.db["users"]))
    cnx.commit()
    cur.execute(sql_templates["get_username"].format(username=username, users_table=constants.db["users"]))
    row = cur.fetchone()
    cur.close()
    return row

@hug.delete('/user/{user_id}')
def delete_user_handler(user_id):
    cur.execute(sql_templates["delete_user"].format(user_id=user_id, users_table=constants.db["users"]))
    db.commit()
    return "Operation successful"

# @hug.post('/game')
# def new_game_handler()
