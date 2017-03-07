import fen
import unittest
from random import randint

class TestCreateFen(unittest.TestCase):
    def setUp(self):
        self.board_width = 8
        self.board_height = 12
        self.expected = "8/8/8/8/8/8/8/8/8/8/8/8 8 12 w 0 0 1"

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
        self.fn = fen.deserialize_row

    def test_values(self):
        self.assertListEqual(fen.deserialize_row(self.input), self.expected)

    def test_length(self):
        self.assertEqual(len(self.expected), len(fen.deserialize_row(self.input)))

    def test_two_digits(self):
        self.assertEqual(len(self.fn('12')), 14)

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
        self.expected_empty_board = {'half_move_clock': 0, 'board_height': 12, 'full_move_clock': 1, 'active_player': 'w', 'board': [{'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': True, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}, {'owner': -1, 'valid': False, 'occupied': False, 'checked': False}], 'board_width': 8, 'stone_count': 0}
        self.non_empty_board = "12/12/3w8/3wb7/3w8/3B8/12/12 12 8 b 0 0 1"

    def test_empty_board(self):
        returned_empty_board = fen.deserialize_fen_string(fen.create_fen(8,12))

    def test_non_empty(self):
        board = fen.deserialize_fen_string(self.non_empty_board)
        self.assertEqual(len(board["board"]), 140)

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

class TestSerializeFenString(unittest.TestCase):
    def setUp(self):
        self.empty_8_by_12 = "8/8/8/8/8/8/8/8/8/8/8/8 8 12 w 0 0 1"

    def test_empty_board(self):
        self.assertEqual(self.empty_8_by_12, fen.serialize_fen_string(fen.deserialize_fen_string(fen.create_fen(8,12))))

    def test_empty_row_count(self):
        random_width = randint(8,13)
        random_height = randint(8,13)
        returned_board = fen.serialize_fen_string(fen.deserialize_fen_string(fen.create_fen(random_width, random_height)))
        self.assertEqual( returned_board.count('/') + 1, random_height)

class TestMoveString(unittest.TestCase):
    def setUp(self):
        self.serialize = fen.serialize_move_string
        self.deserialize = fen.deserialize_move_string

    def test_serialize_simple(self):
        move = ('a1', 'a2')
        expected = 'a1 a2'
        self.assertEqual(self.serialize(*move), expected)

    def test_serialize_jumps(self):
        move = ('a1', 'e1', 'c1')
        expected = 'a1 c1 e1'
        self.assertEqual(self.serialize(*move), expected)

    def test_deserialize_simple(self):
        expected = ('a1', 'a2')
        move = 'a1 a2'
        self.assertEqual(self.serialize(move), expected)

    def test_deserialize_jumps(self):
        expected = ('a1', 'e1', 'c1')
        move = 'a1 c1 e1'
        self.assertEqual(self.serialize(move), expected)

if __name__ == '__main__':
    unittest.main()
