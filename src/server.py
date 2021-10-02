import board, tables
import copy


class Server:
    """Class, that corresponds to chess client bot. It contains tables for the evaluation of moves of various pieces."""

    def evaluate_alphabeta(
        self, board_param, depth, max_best_score, min_best_score, maximizing
    ):
        if depth == 0:
            return self.evaluate(board_param)

        if maximizing:
            best_score = -99999
            for move in board_param.get_possible_moves("white"):
                board_copy = board(board_param)
                board_copy.move_piece_to_position(move)

                best_score = max(
                    best_score,
                    self.alphabeta(
                        board_copy, depth - 1, max_best_score, min_best_score, False
                    ),
                )
                max_best_score = max(max_best_score, best_score)
                if min_best_score <= max_best_score:
                    break
            return best_score
        else:
            best_score = 99999
            for move in board_param.get_possible_moves("black"):
                board_copy = copy.deepcopy(board_param)
                board_copy.move_piece_to_position(move)

                best_score = min(
                    best_score,
                    self.alphabeta(
                        board_copy, depth - 1, max_best_score, min_best_score, True
                    ),
                )
                min_best_score = min(min_best_score, best_score)
                if min_best_score <= max_best_score:
                    break
            return best_score
