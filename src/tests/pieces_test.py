import unittest
from pieces import Bishop, Piece, Rook
from board import Board


class PieciesTest(unittest.TestCase):
    def setUp(self):
        self.pawn = Piece(0, 0, "w", "pawn", 100)
        self.bishop = Bishop(3, 6, "w")
        self.rook = Rook(2, 7, "w")
        self.b = Board(8, 8)

    def test_stringify(self):
        pawn_string = self.pawn.stringify()
        self.assertEqual(pawn_string, "wp")

    def test_get_diagonal_moves(self):
        self.b.initialize_game()
        self.assertEqual(len(self.bishop.get_diagonal_moves(self.b)), 9)

    def test_get_horizontal_moves(self):
        self.b.initialize_game()
        self.assertEqual(len(self.rook.get_horizontal_moves(self.b)), 3)

    def test_clone(self):
        bishop_clone = self.bishop.clone()
        self.assertEqual(bishop_clone.stringify(), "wb")
