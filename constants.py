db = {
    "users": "users"
}

sql_templates = {
    "create_user": """INSERT INTO {users_table} (username)
    SELECT * FROM (SELECT '{username}') AS tmp
    WHERE NOT EXISTS(
	   SELECT username FROM {users_table} WHERE username = '{username}'
   ) LIMIT 1;
   """,
   "get_username": """SELECT * FROM {users_table} WHERE username = '{username}'""",
   "get_user": """SELECT * FROM {users_table} WHERE user_id = {user_id}""",
   "delete_user": """DELETE FROM {users_table} WHERE user_id = {user_id}"""

}
