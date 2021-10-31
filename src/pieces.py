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
        """Getting a string out of piece"""
        piece_type = self.type[1] if self.type == "knight" else self.type[0]
        return self.color[0] + piece_type

    def initialize_move(self, board, xto, yto) -> move.Move:
        """Checking if possible to create move for piece on position and creating if is"""
        initialized_move = 0
        if board.is_piece_bound(xto, yto):
            piece = board.get_piece_position(xto, yto)
            if piece != "-":
                if piece.color != self.color:
                    initialized_move = move.Move(self.x, self.y, xto, yto)
            else:
                initialized_move = move.Move(self.x, self.y, xto, yto)
        return initialized_move

    def get_diagonal_moves(self, board) -> list:
        """Getting all diagonal moves for pieces: Queen, bishop"""
        moves = []

        for i in range(1, board.x):
            if not board.is_piece_bound(self.x + i, self.y - i):
                break

            piece = board.get_piece_position(self.x + i, self.y - i)
            moves.append(self.initialize_move(board, self.x + i, self.y - i))
            if piece != "-":
                break
        for i in range(1, board.x):
            if not board.is_piece_bound(self.x - i, self.y - i):
                break
            piece = board.get_piece_position(self.x - i, self.y - i)
            moves.append(self.initialize_move(board, self.x - i, self.y - i))
            if piece != "-":
                break
        for i in range(1, board.x):
            if not board.is_piece_bound(self.x - i, self.y + i):
                break
            piece = board.get_piece_position(self.x - i, self.y + i)
            moves.append(self.initialize_move(board, self.x - i, self.y + i))
            if piece:
                break
        for i in range(1, board.x):
            if not board.is_piece_bound(self.x + i, self.y + i):
                break
            piece = board.get_piece_position(self.x + i, self.y + i)
            moves.append(self.initialize_move(board, self.x + i, self.y + i))
            if piece != "-":
                break

        return moves

    def get_horizontal_moves(self, board) -> list:
        """Getting all diagonal moves for pieces: Queen, rook"""
        moves = []

        for i in range(1, board.x - self.x):
            piece = board.get_piece_position(self.x + i, self.y)
            moves.append(self.initialize_move(board, self.x + i, self.y))
            if piece:
                break
        for i in range(1, board.x - self.y):
            piece = board.get_piece_position(self.x, self.y + i)
            moves.append(self.initialize_move(board, self.x, self.y + i))
            if piece:
                break
        for i in range(1, self.y + 1):
            piece = board.get_piece_position(self.x, self.y - i)
            moves.append(self.initialize_move(board, self.x, self.y - i))
            if piece:
                break
        for i in range(1, self.x + 1):
            piece = board.get_piece_position(self.x - i, self.y)
            moves.append(self.initialize_move(board, self.x - i, self.y))
            if piece:
                break

        return moves


class Pawn(Piece):
    """Class, that corresponds to a pawn piece"""

    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color, "pawn", 100)
        self.is_in_starting_pos = True

    def get_possible_moves(self, board) -> list:
        """Getting possible moves for piece"""
        moves = []

        direction = -1
        if self.color == "black":
            direction = 1
            if self.y != 1:
                self.is_in_starting_pos = False
        else:
            if self.y != 8 - 2:
                self.is_in_starting_pos = False

        piece = board.get_piece_position(self.x, self.y + direction)
        if piece:
            moves.append(self.initialize_move(board, self.x, self.y + direction))

        two_cells_move = self.y + direction * 2

        if (
            self.is_in_starting_pos
            and board.get_piece_position(self.x, self.y + direction) == "-"
            and board.get_piece_position(self.x, two_cells_move) == "-"
        ):
            moves.append(self.initialize_move(board, self.x, two_cells_move))

        piece = board.get_piece_position(self.x + 1, self.y + direction)
        if piece != "-":
            moves.append(self.initialize_move(board, self.x + 1, self.y + direction))

        piece = board.get_piece_position(self.x - 1, self.y + direction)
        if piece != "-":
            moves.append(self.initialize_move(board, self.x - 1, self.y + direction))

        return moves

    def clone(self):
        """Cloning piece for the evaluation of possible moves"""
        return Pawn(self.x, self.y, self.color)


class Knight(Piece):
    """Class, that corresponds to a knight piece"""

    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color, "knight", 280)

    def get_possible_moves(self, board) -> list:
        """Getting possible moves for piece"""
        moves = []
        moves.append(self.initialize_move(board, self.x - 1, self.y + 2))
        moves.append(self.initialize_move(board, self.x + 2, self.y - 1))
        moves.append(self.initialize_move(board, self.x + 1, self.y + 2))
        moves.append(self.initialize_move(board, self.x + 2, self.y + 1))
        moves.append(self.initialize_move(board, self.x - 2, self.y + 1))
        moves.append(self.initialize_move(board, self.x - 2, self.y - 1))
        moves.append(self.initialize_move(board, self.x - 1, self.y - 2))
        moves.append(self.initialize_move(board, self.x + 1, self.y - 2))
        return moves

    def clone(self):
        """Cloning piece for the evaluation of possible moves"""
        return Knight(self.x, self.y, self.color)


class Bishop(Piece):
    """Class, that corresponds to a bishop piece"""

    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color, "bishop", 320)

    def get_possible_moves(self, board) -> list:
        """Getting possible moves for piece"""
        return self.get_diagonal_moves(board)

    def clone(self):
        """Cloning piece for the evaluation of possible moves"""
        return Bishop(self.x, self.y, self.color)


class Rook(Piece):
    """Class, that corresponds to a rook piece"""

    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color, "rook", 479)

    def get_possible_moves(self, board) -> list:
        """Getting possible moves for piece"""
        return self.get_horizontal_moves(board)

    def clone(self):
        """Cloning piece for the evaluation of possible moves"""
        return Rook(self.x, self.y, self.color)


class Queen(Piece):
    """Class, that corresponds to a queen piece"""

    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color, "queen", 929)

    def get_possible_moves(self, board) -> list:
        """Getting possible moves for piece"""
        diagonal = self.get_diagonal_moves(board)
        horizontal = self.get_horizontal_moves(board)
        return [*diagonal, *horizontal]

    def clone(self):
        """Cloning piece for the evaluation of possible moves"""
        return Queen(self.x, self.y, self.color)


class King(Piece):
    """Class, that corresponds to a king piece"""

    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color, "king", 60000)

    def get_possible_moves(self, board) -> list:
        """Getting possible moves for piece"""
        moves = []

        moves.append(self.initialize_move(board, self.x + 1, self.y))
        moves.append(self.initialize_move(board, self.x - 1, self.y + 1))
        moves.append(self.initialize_move(board, self.x - 1, self.y))
        moves.append(self.initialize_move(board, self.x - 1, self.y - 1))
        moves.append(self.initialize_move(board, self.x, self.y - 1))
        moves.append(self.initialize_move(board, self.x + 1, self.y - 1))
        moves.append(self.initialize_move(board, self.x + 1, self.y + 1))
        moves.append(self.initialize_move(board, self.x, self.y + 1))

        return moves

    def clone(self):
        """Cloning piece for the evaluation of possible moves"""
        return King(self.x, self.y, self.color)
