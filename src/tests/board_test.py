import unittest
from board import Board
import tables


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
        move = self.board.convert_string_to_move("a2-a3")
        self.board.move_piece_to_position(move)
        self.assertNotEqual(self.board.positions_table[ord("a") - 97][-int(3)], "-")

    def test_clone(self):
        self.board.initialize_game()
        board_clone = self.board.clone()
        self.assertEqual(board_clone.x, 8)

    def test_get_possible_moves(self):
        self.board.initialize_game()
        moves = self.board.get_possible_moves()
        self.assertEqual(len(moves), 20)

    def test_evaluate_piece_positions(self):
        self.board.initialize_game()
        move = self.board.convert_string_to_move("a2-a3")
        self.board.move_piece_to_position(move)
        evaluated_pawn_positions = self.board.evaluate_piece_positions(
            "pawn", tables.pawn_table
        )
        self.assertEqual(type(evaluated_pawn_positions), int)

    def test_evaluate_board(self):
        self.board.initialize_game()
        move = self.board.convert_string_to_move("a2-a3")
        self.board.move_piece_to_position(move)
        evaluated_board = self.board.evaluate_board()
        self.assertEqual(type(evaluated_board), int)
        self.assertEqual(evaluated_board, 15)
