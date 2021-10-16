import pieces, tables, move


class Board:
    """Class, that is in charge for dealing with chess board"""

    def __init__(self, x, y, positions_table=[]) -> None:
        self.x = x
        self.y = y
        self.positions_table = positions_table

    def initialize_game(self) -> None:
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

    def draw_situation(self) -> str:
        """Drawing the current situation on board to the terminal"""
        situation = "     A  B  C  D  E  F  G  H\n"
        for vertical in range(self.y):
            situation += str(self.x - vertical) + "   "
            for horizontal in range(self.x):
                piece = self.positions_table[horizontal][vertical]
                if piece != "-":
                    situation += piece.stringify() + " "
                else:
                    situation += ".. "
            situation += "\n"
        return situation + "\n"

    def convert_turn_string_to_move_coord(self, turn) -> move.Move:
        """Converting an input string (example: 'a2-a3') to be returned as Move data structure"""
        [old_position, new_position] = turn.split("-")
        [old_position_char, old_position_num] = list(old_position)
        [new_position_char, new_position_num] = list(new_position)
        return move.Move(
            ord(old_position_char) - 97,
            self.y - int(old_position_num),
            ord(new_position_char) - 97,
            self.y - int(new_position_num),
        )

    def move_piece_to_position(self, mv) -> None:
        """Moving a piece on a certain position to some new position"""
        self.positions_table[mv.xfrom][mv.yfrom].x = mv.xto
        self.positions_table[mv.xfrom][mv.yfrom].y = mv.yto
        self.positions_table[mv.xto][mv.yto] = self.positions_table[mv.xfrom][mv.yfrom]
        self.positions_table[mv.xfrom][mv.yfrom] = "-"

    def get_piece_position(self, x, y) -> str or pieces.Piece:
        """Returning the current piece position on board"""
        if not self.is_piece_bound(x, y):
            return
        return self.positions_table[x][y]

    def is_piece_bound(self, x, y) -> bool:
        """Checking if piece is blocked"""
        return x < self.x and y < self.y and x >= 0 and y >= 0

    def get_possible_moves(self, color="black") -> list:
        """Returning possible moves for pieces on board with a certain color"""
        moves = []
        for x in range(self.x):
            for y in range(self.y):
                piece = self.positions_table[x][y]
                if piece != "-":
                    if piece.color == color:
                        # if piece.type == "pawn":
                        # print(piece)
                        moves += piece.get_possible_moves(self.clone())
        return list(filter(lambda move: move != 0, moves))

    def clone(self):
        """Cloning the board for the evaluation of possible moves"""
        cloned_positions_table = [["-" for _ in range(self.x)] for _ in range(self.y)]
        for x in range(self.x):
            for y in range(self.y):
                piece = self.positions_table[x][y]
                if piece != "-":
                    piece_clone = piece.clone()
                    cloned_positions_table[x][y] = piece_clone
        return Board(self.x, self.y, cloned_positions_table)

    def evaluate_board(self) -> int:
        """Gathering the results of evaluation of possible positions of pieces"""
        pawns = self.evaluate_piece_positions("pawn", tables.pawn_table)
        knights = self.evaluate_piece_positions("knight", tables.knight_table)
        bishops = self.evaluate_piece_positions("bighop", tables.bishop_table)
        rooks = self.evaluate_piece_positions("rook", tables.rook_table)
        queens = self.evaluate_piece_positions("queen", tables.queen_table)
        #print(pawns + knights + bishops + rooks + queens)
        return sum([pawns, knights, bishops, rooks, queens])

    def evaluate_piece_positions(self, piece_type, tbl) -> int:
        """Evaluating of possible positions of pieces"""
        white_pieces = 0
        black_pieces = 0
        for x in range(self.x):
            for y in range(self.y):
                piece = self.positions_table[x][y]
                if piece != "-":
                    if piece.type == piece_type:
                        if piece.color == "white":
                            white_pieces += tbl[x][y]
                        else:
                            black_pieces += tbl[self.x - x - 1][y]

        return white_pieces - black_pieces
