# main.py
import os
import random
from GameManager import Game, GameManager
from TicTacToe import TicTacToe

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
    return Game(game_name)

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

            tic_tac_toe_game = TicTacToe(player_name)
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
