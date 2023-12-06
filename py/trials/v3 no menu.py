import tkinter as tk
import random
from tkinter import messagebox

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

    def make_move(self, position):
        if self.board[position] == "":
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "Tie!")
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

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
