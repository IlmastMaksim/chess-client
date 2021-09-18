import unittest
from pieces import Piece


class PieciesTest(unittest.TestCase):
    def setUp(self):
        self.pawn = Piece(0, 0, "w", "pawn", 100)

    def test_stringify(self):
        pawn_string = self.pawn.stringify()
        self.assertEqual(pawn_string, "wp")
