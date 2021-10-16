import unittest
from server import Server
from pieces import Bishop, Piece, Rook
from board import Board


class ServerTest(unittest.TestCase):
    def setUp(self):
        self.board = Board(8, 8)
        self.board.initialize_game()
        self.serv = Server()
    
    def test_evaluate_optimal_move(self):
        move = self.board.convert_turn_string_to_move_coord("a2-a3")
        self.board.move_piece_to_position(move)
        evaluated_optimal_move = self.serv.evaluate_optimal_move(self.board)
        self.assertEqual(evaluated_optimal_move.xto, 4)
        self.assertEqual(evaluated_optimal_move.yto, 2)