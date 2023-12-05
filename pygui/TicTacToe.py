class TicTacToe:
    def __init__(self, player_name):
        self.player_name = player_name
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def display_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def make_move(self, row, col, symbol):
        if self.board[row][col] == " ":
            self.board[row][col] = symbol
            return True
        return False

    def check_win(self, symbol):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.board[i][j] == symbol for j in range(3)) or all(self.board[j][i] == symbol for j in range(3)):
                return True
        if all(self.board[i][i] == symbol for i in range(3)) or all(self.board[i][2 - i] == symbol for i in range(3)):
            return True
        return False