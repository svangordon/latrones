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
        # # "create_game": """INSERT INTO {game_table} (board_width, board_height) VALUES ({board_width}, {board_height})""",
        # "create_game": """INSERT INTO game () VALUES ();
        # SET @game_id = LAST_INSERT_ID();
        # INSERT INTO participant (game_id, user_id, color) VALUES (@game_id, {user_id}, {color});
        # SET @participant_id = LAST_INSERT_ID();
        # SELECT LAST_INSERT_ID();""",
        # INSERT INTO move (game_id, participant_id, fen) VALUES (@game_id, @participant_id, {fen_string});""",
        "get_game": """SELECT * FROM game WHERE game_id = {game_id};""",
        "get_participants": """SELECT * FROM participant WHERE game_id = {game_id};""",
        "get_moves": """SELECT * FROM move WHERE game_id = {game_id}"""
        # "delete_game": """DELETE FROM {game_table} WHERE game_id = {game_id};
        # SELECT @game_id;""",
        # "get_all_games": """SELECT * FROM {game_table}""",
        # "get_by_user": """SELECT * FROM game WHERE game_id IN (SELECT game_id FROM participant WHERE user_id={user_id});"""
   },
   "participant": {
        "create_participant": """INSERT INTO {participant_table} (game_id, user_id) VALUES ({game_id}, {user_id})""",
        "get_participant_games": """SELECT * FROM {participant_table} where user_id = {user_id}""",
        "delete_participant": """DELETE FROM {participant_table} WHERE participant_id = {participant_id}""",
        "get_participant": """SELECT * FROM {participant_table} WHERE participant_id = {participant_id}""",
        "get_participant_by_user": """SELECT * FROM {participant_table} WHERE user_id = {user_id}"""
    },
    "move" : {
        "get_moves": """SELECT * FROM move WHERE game_id={game_id} ORDER BY half_move_clock""",
        "add_move": """INSERT INTO move (game_id, half_move_clock, notation, position) VALUES ({game_id}, {half_move_clock}, "{notation}", "{position}")""",
        "delete_move": """DELETE FROM move WHERE move_id = {move_id}""",
        "get_move": """SELECT * FROM move WHERE move_id={move_id}"""
    },
    "util": {
        "last_insert": """SELECT LAST_INSERT_ID();"""
    }
}
