import unittest
from board import Board


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board(8, 8)

    def test_initialize_game(self):
        self.board.initialize_game()
        self.assertEqual(len(self.board.positions_table[0]), 8)

    def test_draw_situation(self):
        self.board.initialize_game()
        situation = self.board.draw_situation()
        self.assertTrue("wb" in situation)
        self.assertTrue("bb" in situation)
        self.assertTrue("wk" in situation)

    def test_move_piece_to_position(self):
        self.board.initialize_game()
        self.board.move_piece_to_position("a2-a3")
        self.assertNotEqual(self.board.positions_table[ord("a") - 97][-int(3)], "-")

    def test_clone(self):
        self.board.initialize_game()
        board_clone = self.board.clone()
        self.assertEqual(board_clone.x, 8)

    def test_get_possible_moves(self):
        self.board.initialize_game()
        moves = self.board.get_possible_moves()
        self.assertEqual(len(moves), 14)
