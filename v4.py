import tkinter as tk
from tkinter import simpledialog, messagebox
import random
from datetime import datetime

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [""] * 9

        self.buttons = [tk.Button(self.window, text="", width=10, height=4, command=lambda i=i: self.make_move(i)) for i in range(9)]

        for i in range(3):
            for j in range(3):
                self.buttons[i * 3 + j].grid(row=i, column=j)

        self.set_board_color("white")

        self.player_name = simpledialog.askstring("Player Name", "Enter your name:")
        self.save_results()

        self.save_results_button = tk.Button(self.window, text="Saved Games", command=self.show_saved_games)
        self.save_results_button.grid(row=3, column=0, columnspan=3, pady=10)

        self.change_color_button = tk.Button(self.window, text="Change Board Color", command=self.change_board_color)
        self.change_color_button.grid(row=4, column=0, columnspan=3, pady=10)

    def make_move(self, position):
        if self.board[position] == "":
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)
            if self.check_winner():
                time_won = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_results(time_won, f"Player {self.current_player} wins")
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins at {time_won}!")
                self.reset_board()
            elif "" not in self.board:
                time_tie = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_results(time_tie, "It's a tie!")
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.computer_move()

    def computer_move(self):
        empty_positions = [i for i, value in enumerate(self.board) if value == ""]
        if empty_positions:
            computer_position = random.choice(empty_positions)
            self.make_move(computer_position)

    def check_winner(self):
        for line in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != "":
                return True
        return False

    def reset_board(self):
        for i in range(9):
            self.buttons[i].config(text="")
            self.board[i] = ""
        self.current_player = "X"

    def save_results(self, timestamp=None, result=None):
        if timestamp and result:
            with open("game_results.txt", "a") as file:
                file.write(f"{timestamp}: {self.player_name} - {result}, Board Color: {self.board_color}\n")

    def show_saved_games(self):
        try:
            with open("game_results.txt", "r") as file:
                saved_games = file.read()
                messagebox.showinfo("Saved Games", saved_games)
        except FileNotFoundError:
            messagebox.showinfo("Saved Games", "No saved games yet!")

    def set_board_color(self, color):
        self.board_color = color
        self.window.configure(bg=self.board_color)

    def change_board_color(self):
        color = simpledialog.askstring("Change Board Color", "Enter a color name:")
        if color:
            self.set_board_color(color)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
