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

if __name__ == '__main__':
    unittest.main()
