#chess game 
#Lwazi Somtsewu

class ChessPiece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return self.name[0].upper() if self.color == "white" else self.name[0].lower()


class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Create an 8x8 chess board
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Set up pieces for white
        board[0] = [
            ChessPiece("white", "rook"), ChessPiece("white", "knight"), ChessPiece("white", "bishop"),
            ChessPiece("white", "queen"), ChessPiece("white", "king"), ChessPiece("white", "bishop"),
            ChessPiece("white", "knight"), ChessPiece("white", "rook")
        ]
        board[1] = [ChessPiece("white", "pawn") for _ in range(8)]

        # Set up pieces for black
        board[7] = [
            ChessPiece("black", "rook"), ChessPiece("black", "knight"), ChessPiece("black", "bishop"),
            ChessPiece("black", "queen"), ChessPiece("black", "king"), ChessPiece("black", "bishop"),
            ChessPiece("black", "knight"), ChessPiece("black", "rook")
        ]
        board[6] = [ChessPiece("black", "pawn") for _ in range(8)]

        return board

    def display(self):
        for row in self.board:
            print(" ".join(str(piece) if piece else '.' for piece in row))
        print()

    def move_piece(self, start, end):
        start_x, start_y = start
        end_x, end_y = end

        if self.is_valid_move(start, end):
            piece = self.board[start_x][start_y]
            self.board[end_x][end_y] = piece
            self.board[start_x][start_y] = None
            return True
        return False

    def is_valid_move(self, start, end):
        start_x, start_y = start
        end_x, end_y = end

        # Basic validation: Ensure start and end are within bounds
        if not all(0 <= i < 8 for i in [start_x, start_y, end_x, end_y]):
            return False
        
        # Ensure the start square has a piece
        if self.board[start_x][start_y] is None:
            return False
        
        # Ensure the end square is either empty or occupied by an opponent's piece
        target_piece = self.board[end_x][end_y]
        if target_piece and target_piece.color == self.board[start_x][start_y].color:
            return False

        # More advanced movement rules would go here (e.g., piece-specific movements)
        
        return True


def main():
    chess_board = ChessBoard()
    chess_board.display()

    while True:
        move = input("Enter your move (e.g., 'a2 a3' or 'exit' to quit): ").strip()
        if move.lower() == 'exit':
            break

        try:
            start, end = move.split()
            start_x, start_y = 8 - int(start[1]), ord(start[0]) - ord('a')
            end_x, end_y = 8 - int(end[1]), ord(end[0]) - ord('a')
            if chess_board.move_piece((start_x, start_y), (end_x, end_y)):
                chess_board.display()
            else:
                print("Invalid move. Please try again.")
        except (ValueError, IndexError):
            print("Invalid input. Use the format 'a2 a3'.")


if __name__ == "__main__":
    main()
