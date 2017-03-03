db = {
    "users": "user",
    "game": "game",
    "participant": "participant"
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
   },
   "game": {
        "create_game": """INSERT INTO {game_table} (board_width, board_height) VALUES ({board_width}, {board_height})""",
        "delete_game": """DELETE FROM {game_table} WHERE game_id = {game_id}""",
        "get_all_games": """SELECT * FROM {game_table}""",
        "get_game_by_id": """SELECT * FROM {game_table} WHERE game_id = {game_id}""",
        "get_by_user": """SELECT * FROM game WHERE game_id IN (SELECT game_id FROM participant WHERE user_id={user_id});"""
   },
   "participant": {
        "create_participant": """INSERT INTO {participant_table} (game_id, user_id) VALUES ({game_id}, {user_id})""",
        "get_participant_games": """SELECT * FROM {participant_table} where user_id = {user_id}""",
        "delete_participant": """DELETE FROM {participant_table} WHERE participant_id = {participant_id}""",
        "get_participant": """SELECT * FROM {participant_table} WHERE participant_id = {participant_id}""",
        "get_participant_by_user": """SELECT * FROM {participant_table} WHERE user_id = {user_id}"""
    },
    "util": {
        "last_insert": """SELECT LAST_INSERT_ID();"""
    }
}
