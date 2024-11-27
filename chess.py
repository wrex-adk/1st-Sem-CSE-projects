class Piece:
    def __init__(self, color):
        self.color = color

    def is_valid_move(self, start, end, board):
        raise NotImplementedError("Please implement this method in subclasses")

class Pawn(Piece):
    def is_valid_move(self, start, end, board):
        direction = 1 if self.color == 'white' else -1
        if start[1] == end[1] and (end[0] - start[0] == direction):
            return board[end[0]][end[1]] == ' '  # Normal move forward
        elif abs(end[1] - start[1]) == 1 and end[0] - start[0] == direction:
            return isinstance(board[end[0]][end[1]], Piece) and board[end[0]][end[1]].color != self.color  # Capture move
        return False

class Rook(Piece):
    def is_valid_move(self, start, end, board):
        if start[0] == end[0] or start[1] == end[1]:
            return True
        return False

class Knight(Piece):
    def is_valid_move(self, start, end, board):
        return (abs(start[0] - end[0]), abs(start[1] - end[1])) in [(2, 1), (1, 2)]

class Bishop(Piece):
    def is_valid_move(self, start, end, board):
        return abs(start[0] - end[0]) == abs(start[1] - end[1])

class Queen(Piece):
    def is_valid_move(self, start, end, board):
        return Rook(self.color).is_valid_move(start, end, board) or Bishop(self.color).is_valid_move(start, end, board)

class King(Piece):
    def is_valid_move(self, start, end, board):
        return max(abs(start[0] - end[0]), abs(start[1] - end[1])) == 1

class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.turn = 'white'

    def initialize_board(self):
        board = [[' ' for _ in range(8)] for _ in range(8)]
        # Place Pawns
        for i in range(8):
            board[1][i] = Pawn('white')
            board[6][i] = Pawn('black')
        # Place Rooks
        board[0][0] = board[0][7] = Rook('white')
        board[7][0] = board[7][7] = Rook('black')
        # Place Knights
        board[0][1] = board[0][6] = Knight('white')
        board[7][1] = board[7][6] = Knight('black')
        # Place Bishops
        board[0][2] = board[0][5] = Bishop('white')
        board[7][2] = board[7][5] = Bishop('black')
        # Place Queens
        board[0][3] = Queen('white')
        board[7][3] = Queen('black')
        # Place Kings
        board[0][4] = King('white')
        board[7][4] = King('black')
        return board

    def print_board(self):
        for row in self.board:
            print(' '.join([str(piece.__class__.__name__[0] if piece != ' ' else '.' for piece in row)]))
        print()

    def move_piece(self, start, end):
        piece = self.board[start[0]][start[1]]
        if piece != ' ' and piece.color == self.turn:
            if piece.is_valid_move(start, end, self.board):
                self.board[end[0]][end[1]] = piece
                self.board[start[0]][start[1]] = ' '
                self.turn = 'black' if self.turn == 'white' else 'white'
            else:
                print("Invalid move")
        else:
            print("Invalid piece or turn")

    def start(self):
        while True:
            self.print_board()
            start = input(f"{self.turn.capitalize()}'s turn - Enter start position (e.g., 1 0): ")
            end = input(f"Enter end position (e.g., 2 0): ")
            start = tuple(map(int, start.split()))
            end = tuple(map(int, end.split()))
            self.move_piece(start, end)

if __name__ == "__main__":
    game = ChessGame()
    game.start()
