import fen
import unittest

class TestCreateFen(unittest.TestCase):
    def setUp(self):
        self.board_width = 8
        self.board_height = 12
        self.expected = "8/8/8/8/8/8/8/8/8/8/8/8 8 12 w 0 d 0 1"

    def test_value(self):
        self.assertEqual(fen.create_fen(self.board_width, self.board_height), self.expected)

class TestCharGenerator(unittest.TestCase):
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
        self.assertListEqual(self.expected, list(map(fen.char_generator, self.input)))

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

if __name__ == '__main__':
    unittest.main()
