db = {
    "users": "user"
}

sql_templates = {
    "create_user": """INSERT INTO {users_table} (username) VALUES ('{username}');""",
   "get_username": """SELECT * FROM {users_table} WHERE username = '{username}'""",
   "get_user": """SELECT * FROM {users_table} WHERE user_id = {user_id}""",
   "delete_user": """DELETE FROM {users_table} WHERE user_id = {user_id}""",
   "user": {
       "create_user": """INSERT INTO {users_table} (username) VALUES ('{username}');""",
       "get_username": """SELECT * FROM {users_table} WHERE username = '{username}'""",
        "get_user": """SELECT * FROM {users_table} WHERE user_id = {user_id}""",
        "delete_user": """DELETE FROM {users_table} WHERE user_id = {user_id}""",
        "get_all": """SELECT * FROM {users_table}"""
   }
}
