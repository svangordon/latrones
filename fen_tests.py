import fen
import unittest

class TestCreateFen(unittest.TestCase):
    def setUp(self):
        self.board_width = 8
        self.board_height = 12
        self.expected = "8/8/8/8/8/8/8/8/8/8/8/8 8 12 w 0 d 0 1"

    def test_value(self):
        self.assertEqual(fen.create_fen(self.board_width, self.board_height), self.expected)

class TestGenerateSquare(unittest.TestCase):
    def setUp(self):
        self.input = [-1, 'w', 'W', 'b', 'B', None]
        self.expected = [
        {'owner': -1, 'occupied': False, 'valid': False, 'checked': False},
        {'owner': 0, 'valid': True, 'occupied': True, 'checked': False},
        {'valid': True, 'occupied': True, 'owner': 0, 'checked': True},
        {'owner': 1, 'valid': True, 'checked': False, 'occupied': True},
        {'checked': True, 'valid': True, 'occupied': True, 'owner': 1},
        {'owner': -1, 'valid': True, 'checked': False, 'occupied': False}
        ]

    def test_values(self):
        self.assertListEqual(self.expected, list(map(fen.generate_square, self.input)))

class TestGenerateChar(unittest.TestCase):
    def setUp(self):
        self.input = [{'owner': -1, 'occupied': False, 'valid': False, 'checked': False},
        {'owner': 0, 'valid': True, 'occupied': True, 'checked': False},
        {'valid': True, 'occupied': True, 'owner': 0, 'checked': True},
        {'owner': 1, 'valid': True, 'checked': False, 'occupied': True},
        {'checked': True, 'valid': True, 'occupied': True, 'owner': 1},
        {'owner': -1, 'valid': True, 'checked': False, 'occupied': False}]
        self.expected = ['', 'w', 'W', 'b', 'B', '1']

    def test_values(self):
        self.assertListEqual(self.expected, list(map(fen.generate_char, self.input)))

class TestDeserializeChar(unittest.TestCase):
    def setUp(self):
        self.input = [3, 'w', 'W', 'b', 'B']
        self.expected = [[{'occupied': False, 'valid': True, 'owner': -1, 'checked': False}, {'occupied': False, 'valid': True, 'owner': -1, 'checked': False}, {'occupied': False, 'valid': True, 'owner': -1, 'checked': False}], [{'occupied': True, 'valid': True, 'owner': 0, 'checked': False}], [{'occupied': True, 'valid': True, 'owner': 0, 'checked': True}], [{'occupied': True, 'valid': True, 'owner': 1, 'checked': False}], [{'occupied': True, 'valid': True, 'owner': 1, 'checked': True}]]

    def test_values(self):
        self.assertListEqual(self.expected, list(map(fen.deserialize_char, self.input)))

class TestDeserializeRow(unittest.TestCase):
    def setUp(self):
        self.input = "1wW1bB3"
        self.expected = [{'checked': False, 'valid': False, 'occupied': False, 'owner': -1}, {'checked': False, 'valid': True, 'occupied': False, 'owner': -1}, {'checked': False, 'valid': True, 'occupied': True, 'owner': 0}, {'checked': True, 'valid': True, 'occupied': True, 'owner': 0}, {'checked': False, 'valid': True, 'occupied': False, 'owner': -1}, {'checked': False, 'valid': True, 'occupied': True, 'owner': 1}, {'checked': True, 'valid': True, 'occupied': True, 'owner': 1}, {'checked': False, 'valid': True, 'occupied': False, 'owner': -1}, {'checked': False, 'valid': True, 'occupied': False, 'owner': -1}, {'checked': False, 'valid': True, 'occupied': False, 'owner': -1}, {'checked': False, 'valid': False, 'occupied': False, 'owner': -1}]

    def test_values(self):
        self.assertListEqual(fen.deserialize_row(self.input), self.expected)

    def test_length(self):
        self.assertEqual(len(self.expected), len(fen.deserialize_row(self.input)))

class TestDeserializeBoardString(unittest.TestCase):
    def setUp(self):
        self.board_width = 8
        self.board_height = 12
        self.expected_empty_board = [{'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': True, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}, {'owner': -1, 'occupied': False, 'valid': False, 'checked': False}]
        self.empty_input = "8/8/8/8/8/8/8/8/8/8/8/8"

    def test_empty_board_content(self):
        returned_empty_board = fen.deserialize_board_string(self.empty_input)
        self.assertListEqual(self.expected_empty_board, returned_empty_board)

    def test_empty_board_length(self):
        expected_empty_board_len = (self.board_width + 2)*(self.board_height + 2)
        self.assertEqual(expected_empty_board_len, len(fen.deserialize_board_string(self.empty_input)))

class TestDeserializeFenString(unittest.TestCase):
    def setUp(self):
        self.board_width = 8
        self.board_height = 12
        self.expected_empty_board = {'halfmoveClock': 0, 'boardHeight': 12, 'gamePhase': 'd', 'fullMoveClock': 1, 'activePlayer': 'w', 'boardString': [{'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}], 'boardWidth': 8, 'stoneCount': 0}

    def test_empty_board(self):
        returned_empty_board = fen.deserialize_fen_string(fen.create_fen(8,12))

class TestCharConversion(unittest.TestCase):
    def test_convert_w(self):
        self.assertEqual('w', fen.generate_char(fen.generate_square('w')))

    def test_convert_empty(self):
        self.assertEqual('1', fen.generate_char(fen.generate_square()))

class TestSerializeBoardString(unittest.TestCase):
    def setUp(self):
        self.empty_board_input = [{'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': True}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}, {'owner': -1, 'checked': False, 'occupied': False, 'valid': False}]
        self.expected_empty_board = '8/8/8/8/8/8/8/8/8/8/8/8'

    def test_empty_board(self):
        self.assertEqual(self.expected_empty_board, fen.serialize_board_string(self.empty_board_input))

if __name__ == '__main__':
    unittest.main()
