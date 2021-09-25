import pieces


class Board:
    """Class, that is in charge for dealing with chess board"""

    def __init__(self, x, y, positions_table=[]) -> None:
        self.x = x
        self.y = y
        self.positions_table = positions_table

    def initialize_game(self):
        """Initialization of the default settings of the game"""
        self.positions_table = [["-" for _ in range(self.x)] for _ in range(self.y)]
        for x_pos in range(self.x):
            self.positions_table[x_pos][self.x - 2] = pieces.Pawn(
                x_pos, self.x - 2, "white"
            )
            self.positions_table[x_pos][1] = pieces.Pawn(x_pos, 1, "black")

        self.positions_table[1][0] = pieces.Knight(1, 0, "black")
        self.positions_table[1][self.y - 1] = pieces.Knight(1, self.y - 1, "white")
        self.positions_table[self.x - 2][0] = pieces.Knight(self.x - 2, 0, "black")
        self.positions_table[self.x - 2][self.y - 1] = pieces.Knight(
            self.x - 2, self.y - 1, "white"
        )

        self.positions_table[2][0] = pieces.Bishop(2, 0, "black")
        self.positions_table[2][self.y - 1] = pieces.Bishop(2, self.y - 1, "white")
        self.positions_table[self.x - 3][0] = pieces.Bishop(self.x - 3, 0, "black")
        self.positions_table[self.x - 3][self.y - 1] = pieces.Bishop(
            self.x - 3, self.y - 1, "white"
        )

        self.positions_table[0][self.y - 1] = pieces.Rook(0, self.y - 1, "white")
        self.positions_table[0][0] = pieces.Rook(0, 0, "black")
        self.positions_table[self.x - 1][self.y - 1] = pieces.Rook(
            self.x - 1, self.y - 1, "white"
        )
        self.positions_table[self.x - 1][0] = pieces.Rook(self.x - 1, 0, "black")

        self.positions_table[4][self.y - 1] = pieces.King(4, self.y - 1, "white")
        self.positions_table[3][self.y - 1] = pieces.Queen(3, self.y - 1, "white")
        self.positions_table[4][0] = pieces.King(4, 0, "black")
        self.positions_table[3][0] = pieces.Queen(3, 0, "black")

    def draw_situation(self):
        """Drawing the current situation on board to the terminal"""
        situation = "     A  B  C  D  E  F  G  H\n"
        for vertical in range(self.y):
            situation += str(8 - vertical) + "   "
            for horizontal in range(self.x):
                piece = self.positions_table[horizontal][vertical]
                if piece != "-":
                    situation += piece.stringify() + " "
                else:
                    situation += ".. "
            situation += "\n"
        return situation + "\n"

    def move_piece_to_position(self, turn):
        """Moving a piece on a certain position to some new position"""
        # example: a2-a3
        [old_position, new_position] = turn.split("-")
        [old_position_char, old_position_num] = list(old_position)
        [new_position_char, new_position_num] = list(new_position)
        self.positions_table[ord(old_position_char) - 97][-int(old_position_num)].x = (
            ord(new_position_char) - 97
        )
        self.positions_table[ord(old_position_char) - 97][
            -int(old_position_num)
        ].y = -int(new_position_num)
        self.positions_table[ord(new_position_char) - 97][
            -int(new_position_num)
        ] = self.positions_table[ord(old_position_char) - 97][-int(old_position_num)]
        self.positions_table[ord(old_position_char) - 97][-int(old_position_num)] = "-"

    def get_piece_position(self, x, y):
        """Returning the current piece position on board"""
        return self.positions_table[x][y]

    def get_possible_moves(self, color="black"):
        moves = []
        for x in range(self.x):
            for y in range(self.y):
                piece = self.positions_table[x][y]
                if piece != "-":
                    if piece.color == color:
                        if piece.type == "pawn":
                            # print(piece)
                            moves += piece.get_possible_moves(self.clone())
        return moves

    def clone(self):
        cloned_positions_table = [["-" for _ in range(self.x)] for _ in range(self.y)]
        for x in range(self.x):
            for y in range(self.y):
                piece = self.positions_table[x][y]
                if piece != "-":
                    cloned_positions_table[x][y] = piece.clone()
        return Board(self.x, self.y, cloned_positions_table)
