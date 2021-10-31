from move import Move


class Server:
    """Class, that is in charge for dealing with chess client"""

    def evaluate_optimal_move(self, board_param) -> Move:
        """Providing the board with the most optimal move generated by alphabeta"""
        optimal_move = 0
        optimal_score = 999999
        for possible_move in board_param.get_possible_moves("black"):
            cloned_board = board_param.clone()
            cloned_board.move_piece_to_position(possible_move)

            score = self.alphabeta(cloned_board, 2, -999999, 999999, True)
            if score < optimal_score:
                optimal_score = score
                optimal_move = possible_move

        if optimal_move == 0:
            return 0

        cloned_board = board_param.clone()
        cloned_board.move_piece_to_position(optimal_move)

        return optimal_move

    def alphabeta(self, board_param, depth, alpha, beta, maximizing) -> int:
        """Algorithm that decreases the number of possible moves to select the most optimal one"""
        if depth == 0:
            return board_param.evaluate_board()

        if maximizing:
            optimal_score = -999999
            for possible_move in board_param.get_possible_moves("white"):
                cloned_board = board_param.clone()
                cloned_board.move_piece_to_position(possible_move)

                optimal_score = max(
                    optimal_score,
                    self.alphabeta(cloned_board, depth - 1, alpha, beta, False),
                )
                alpha = max(alpha, optimal_score)
                if beta <= alpha:
                    break
            return optimal_score
        else:
            optimal_score = 999999
            for possible_move in board_param.get_possible_moves("black"):
                cloned_board = board_param.clone()
                cloned_board.move_piece_to_position(possible_move)

                optimal_score = min(
                    optimal_score,
                    self.alphabeta(cloned_board, depth - 1, alpha, beta, True),
                )
                beta = min(beta, optimal_score)
                if beta <= alpha:
                    break
            return optimal_score
