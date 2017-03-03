import fen
import unittest

class TestCreateFen(unittest.TestCase):
    def setUp(self):
        self.board_width = 8
        self.board_height = 12
        self.expected = "8/8/8/8/8/8/8/8/8/8/8/8 8 12 w 0 d 0 1"

    def test_value(self):
        self.assertEqual(fen.create_fen(self.board_width, self.board_height), self.expected)

if __name__ == '__main__':
    unittest.main()
