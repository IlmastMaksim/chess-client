import board

if __name__ == "__main__":
    initialized_board = board.Board(8, 8)
    initialized_board.initialize_game()
    initialized_board.move_piece_to_position("a2-a3")
    initialized_board.draw_situation()
    # while True:
    #    turn = input("Type your turn: ")
    #    initialized_board.draw_situation()
