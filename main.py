# main.py
import os
import random

class Game:
    def __init__(self, name, board_color):
        self.name = name
        self.board_color = board_color
        self.status = "Active"

class GameManager:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def display_games(self):
        for game in self.games:
            print(f"Name: {game.name}, Color: {game.board_color}, Status: {game.status}")

class TicTacToe:
    def __init__(self, player_name, board_color):
        self.player_name = player_name
        self.board_color = board_color
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

def initialize_game():
    if not os.path.exists("player_name.txt"):
        name = input("Enter your name: ")
        with open("player_name.txt", "w") as file:
            file.write(name)

def get_player_name():
    with open("player_name.txt", "r") as file:
        return file.read().strip()

def create_game():
    game_name = input("Enter game name: ")
    board_color = input("Enter board background color: ")
    return Game(game_name, board_color)

def main():
    initialize_game()
    player_name = get_player_name()
    print(f"Hello, {player_name}!")

    game_manager = GameManager()

    while True:
        print("\n1. Create a new game")
        print("2. Display list of games")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            new_game = create_game()
            game_manager.add_game(new_game)
            print(f"Game created: {new_game.name}")

            tic_tac_toe_game = TicTacToe(player_name, new_game.board_color)
            tic_tac_toe_game.display_board()

            while True:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))

                if tic_tac_toe_game.make_move(row, col, "X"):
                    tic_tac_toe_game.display_board()
                    if tic_tac_toe_game.check_win("X"):
                        print("Congratulations! You won!")
                        new_game.status = "Completed"
                        break

                    # Computer's move
                    computer_row, computer_col = random.choice([(i, j) for i in range(3) for j in range(3) if tic_tac_toe_game.board[i][j] == " "])
                    tic_tac_toe_game.make_move(computer_row, computer_col, "O")
                    print("Computer's move:")
                    tic_tac_toe_game.display_board()

                    if tic_tac_toe_game.check_win("O"):
                        print("Computer wins! Better luck next time.")
                        new_game.status = "Completed"
                        break

                else:
                    print("Invalid move. Try again.")

        elif choice == "2":
            game_manager.display_games()

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
