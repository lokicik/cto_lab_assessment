import os
import random
import tkinter as tk
from tkinter import messagebox

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
        game_info = ""
        for game in self.games:
            game_info += f"Name: {game.name}, Color: {game.board_color}, Status: {game.status}\n"
        return game_info

class TicTacToe:
    def __init__(self, player_name, board_color):
        self.player_name = player_name
        self.board_color = board_color
        self.board = [[" " for _ in range(3)] for _ in range(3)]

class TicTacToeGUI:
    def __init__(self, root, player_name, board_color):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player_name = player_name
        self.board_color = board_color
        self.game_manager = GameManager()

        self.create_widgets()


    def create_widgets(self):
        self.label = tk.Label(self.root, text=f"Hello, {self.player_name}!")
        self.label.pack()

        self.new_game_button = tk.Button(self.root, text="Create a new game", command=self.create_new_game)
        self.new_game_button.pack()

        self.display_games_button = tk.Button(self.root, text="Display list of games", command=self.display_games)
        self.display_games_button.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.pack()

    def create_new_game(self):
        game_name = input("Enter game name: ")
        board_color = input("Enter board background color: ")

        new_game = Game(game_name, board_color)
        self.game_manager.add_game(new_game)

        tic_tac_toe_game = TicTacToe(self.player_name, new_game.board_color)
        self.play_tic_tac_toe(tic_tac_toe_game)

    def display_games(self):
        games_info = self.game_manager.display_games()
        messagebox.showinfo("Game List", games_info)

    def play_tic_tac_toe(self, tic_tac_toe_game):
        tic_tac_toe_window = tk.Toplevel(self.root)
        tic_tac_toe_window.title("Tic Tac Toe Game")

        for i in range(3):
            for j in range(3):
                button = tk.Button(tic_tac_toe_window, text="", width=10, height=3, command=lambda i=i, j=j: self.make_move(tic_tac_toe_game, tic_tac_toe_window, i, j))
                button.grid(row=i, column=j)

    def make_move(self, tic_tac_toe_game, tic_tac_toe_window, row, col):
        if tic_tac_toe_game.board[row][col] == " ":
            tic_tac_toe_game.board[row][col] = "X"
            button = tic_tac_toe_window.grid_slaves(row=row, column=col)[0]
            button.config(text="X", state=tk.DISABLED)

            if self.check_win(tic_tac_toe_game, "X"):
                messagebox.showinfo("Game Over", "Congratulations! You won!")
                tic_tac_toe_window.destroy()
            else:
                computer_move(tic_tac_toe_game, tic_tac_toe_window)

    def check_win(self, tic_tac_toe_game, symbol):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(tic_tac_toe_game.board[i][j] == symbol for j in range(3)) or all(tic_tac_toe_game.board[j][i] == symbol for j in range(3)):
                return True
        if all(tic_tac_toe_game.board[i][i] == symbol for i in range(3)) or all(tic_tac_toe_game.board[i][2 - i] == symbol for i in range(3)):
            return True
        return False

def computer_move(tic_tac_toe_game, tic_tac_toe_window):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if tic_tac_toe_game.board[i][j] == " "]
    if empty_cells:
        computer_row, computer_col = random.choice(empty_cells)
        tic_tac_toe_game.board[computer_row][computer_col] = "O"
        button = tic_tac_toe_window.grid_slaves(row=computer_row, column=computer_col)[0]
        button.config(text="O", state=tk.DISABLED)

        if tic_tac_toe_game.check_win("O"):
            messagebox.showinfo("Game Over", "Computer wins! Better luck next time.")
            tic_tac_toe_window.destroy()

def main():
    root = tk.Tk()
    tic_tac_toe_gui = TicTacToeGUI(root, "Player", "lightgrey")
    root.mainloop()

if __name__ == "__main__":
    main()
