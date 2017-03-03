import unittest
import game_logic
import fen

class TestMoveValidation(unittest.TestClass):
    def test_no_move_from_in_deployment(self):
        self.assertFalse(game_logic.validate_move(fen.create_fen(), 5, 5))

if __name__ == '__main__':
    unittest.main()
