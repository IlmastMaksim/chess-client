import board, server


class Game:
    """Class, that is in charge for initializing and running the game"""

    def __init__(self) -> None:
        self.board = board.Board(8, 8)
        self.server = server.Server()

    def run(self) -> None:
        """Initializing and running the game"""
        self.board.initialize_game()
        while True:
            was_checkmate = self.board.check_for_checkmate()
            if was_checkmate != "":
                print(was_checkmate)
            else:
                print(self.board.draw_situation())
                player_turn = input("Enter your move (e.g e2-e3): ")
                try:
                    move = self.board.convert_string_to_move(player_turn)
                    self.board.move_piece_to_position(move)
                    evaluated_optimal_move = self.server.evaluate_optimal_move(
                        self.board
                    )
                    self.board.move_piece_to_position(evaluated_optimal_move)
                except:
                    print()


if __name__ == "__main__":
    game = Game()
    game.run()
