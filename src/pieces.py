import move


class Piece:
    """Class, that corresponds to a chess piece"""

    def __init__(self, x, y, color, type, value) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.type = type
        self.value = value

    def stringify(self) -> str:
        return self.color[0] + self.type[0]

    def initialize_move(self, xto, yto) -> move.Move:
        initialized_move = move.Move(self.x, self.y, xto, yto)
        return initialized_move


class Pawn(Piece):
    """Class, that corresponds to a pawn piece"""

    def __init__(self, x, y, color) -> None:
        super(Pawn, self).__init__(x, y, color, "pawn", 100)

    def get_possible_moves(self, board):
        moves = []

        direction = -1
        if self.color == "black":
            direction = 1

        if board.get_piece_position(self.x, self.y + direction) == 0:
            moves.append(self.initialize_move(self.x, self.y))

        return moves

    def clone(self):
        return Pawn(self.x, self.y, self.color)


class Knight(Piece):
    """Class, that corresponds to a knight piece"""

    def __init__(self, x, y, color) -> None:
        super(Knight, self).__init__(x, y, color, "knight", 280)

    def get_possible_moves(self, board):
        moves = []
        return moves

    def clone(self):
        return Knight(self.x, self.y, self.color)


class Bishop(Piece):
    """Class, that corresponds to a bishop piece"""

    def __init__(self, x, y, color) -> None:
        super(Bishop, self).__init__(x, y, color, "bishop", 320)

    def get_possible_moves(self, board):
        moves = []
        return moves

    def clone(self):
        return Bishop(self.x, self.y, self.color)


class Rook(Piece):
    """Class, that corresponds to a rook piece"""

    def __init__(self, x, y, color) -> None:
        super(Rook, self).__init__(x, y, color, "rook", 479)

    def get_possible_moves(self, board):
        moves = []
        return moves

    def clone(self):
        return Rook(self.x, self.y, self.color)


class Queen(Piece):
    """Class, that corresponds to a queen piece"""

    def __init__(self, x, y, color) -> None:
        super(Queen, self).__init__(x, y, color, "queen", 929)

    def get_possible_moves(self, board):
        moves = []
        return moves

    def clone(self):
        return Queen(self.x, self.y, self.color)


class King(Piece):
    """Class, that corresponds to a king piece"""

    def __init__(self, x, y, color) -> None:
        super(King, self).__init__(x, y, color, "king", 60000)

    def get_possible_moves(self, board):
        moves = []
        return moves

    def clone(self):
        return King(self.x, self.y, self.color)
