import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
import random
from datetime import datetime

class SingletonApp(tk.Tk):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class GameCreateScreen:
    def __init__(self, root, player_name):
        self.root = root
        self.root.title("Game Create Screen")

        self.player_name = player_name

        # Check if there is an active game
        self.continue_game = False
        self.active_game_label = tk.Label(self.root, text="No active game")
        self.active_game_label.pack(pady=10)

        # Check if there is an active game
        self.check_active_game()

        self.create_game_button = tk.Button(self.root, text="Continue to Game" if self.continue_game else "Create Game", command=self.create_game)
        self.create_game_button.pack(pady=10)

    def create_game(self):
        self.root.withdraw()  # Hide the main window
        game_window = tk.Toplevel(self.root)
        game_window.title("Game Screen")
        game_screen = GameScreen(game_window, self.player_name)

    def check_active_game(self):
        try:
            with open("active_game.txt", "r") as file:
                active_game_data = file.readline().strip()
                if active_game_data:
                    self.continue_game = True
                    self.active_game_label.config(text=f"Active game: {active_game_data}")
        except FileNotFoundError:
            pass

class ListOfGamesScreen:
    def __init__(self, root, player_name):
        self.root = root
        self.root.title("List of Games Screen")

        self.player_name = player_name

        self.show_saved_games()

        self.back_to_main_button = tk.Button(self.root, text="Back to Main Menu", command=self.back_to_main)
        self.back_to_main_button.pack(pady=10)

    def show_saved_games(self):
        try:
            with open("game_results.txt", "r") as file:
                saved_games = file.readlines()
                filtered_games = [game for game in saved_games if self.player_name in game]
                if filtered_games:
                    games_text = "\n".join(filtered_games)
                    games_scrolltext = scrolledtext.ScrolledText(self.root, width=40, height=15, wrap=tk.WORD)
                    games_scrolltext.insert(tk.END, games_text)
                    games_scrolltext.pack()
                else:
                    no_games_label = tk.Label(self.root, text=f"No games found for {self.player_name}.")
                    no_games_label.pack()
        except FileNotFoundError:
            no_games_label = tk.Label(self.root, text="No saved games yet!")
            no_games_label.pack()

    def back_to_main(self):
        self.root.destroy()  # Close the List of Games Screen
        app.deiconify()  # Show the main window

class GameScreen:
    def __init__(self, root, player_name):
        self.root = root
        self.root.title("Game Screen")

        self.player_name = player_name

        self.current_player = "X"
        self.board_size = 4  # Size of the board (4x4)
        self.board = [""] * (self.board_size ** 2)

        self.buttons = [tk.Button(self.root, text="", width=8, height=2, command=lambda i=i: self.make_move(i)) for i in range(self.board_size ** 2)]

        for i in range(self.board_size):
            for j in range(self.board_size):
                self.buttons[i * self.board_size + j].grid(row=i, column=j)

        self.set_board_color("white")

        self.save_results_button = tk.Button(self.root, text="Saved Games", command=self.show_saved_games)
        self.save_results_button.grid(row=self.board_size, column=0, columnspan=self.board_size, pady=10)

        self.change_color_button = tk.Button(self.root, text="Change Board Color", command=self.change_board_color)
        self.change_color_button.grid(row=self.board_size + 1, column=0, columnspan=self.board_size, pady=10)

        self.return_to_main_button = tk.Button(self.root, text="Return to Main Menu", command=self.return_to_main)
        self.return_to_main_button.grid(row=self.board_size + 2, column=0, columnspan=self.board_size, pady=10)

        self.close_program_button = tk.Button(self.root, text="Close Program", command=self.close_program)
        self.close_program_button.grid(row=self.board_size + 3, column=0, columnspan=self.board_size, pady=10)

        self.save_active_game()

    def save_active_game(self):
        with open("active_game.txt", "w") as file:
            file.write(f"Player: {self.player_name}, Current Player: {self.current_player}")

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
                    self.computer_move()  # Trigger computer move after the player

    def computer_move(self):
        empty_positions = [i for i, value in enumerate(self.board) if value == ""]
        if empty_positions:
            computer_position = random.choice(empty_positions)
            self.make_move(computer_position)

    def check_winner(self):
        for i in range(self.board_size):
            # Check rows and columns
            if len(set(self.board[i * self.board_size: (i + 1) * self.board_size])) == 1 and self.board[i * self.board_size] != "":
                return True
            if len(set(self.board[i::self.board_size])) == 1 and self.board[i] != "":
                return True

        # Check diagonals
        if len(set(self.board[::self.board_size + 1])) == 1 and self.board[0] != "":
            return True
        if len(set(self.board[self.board_size - 1::self.board_size - 1])) == 1 and self.board[self.board_size - 1] != "":
            return True

        return False

    def reset_board(self):
        for i in range(self.board_size ** 2):
            self.buttons[i].config(text="")
            self.board[i] = ""
        self.current_player = "X"
        self.clear_active_game()

    def save_results(self, timestamp, result):
        with open("game_results.txt", "a") as file:
            file.write(f"{timestamp}: {self.player_name} - {result}, Board Color: {self.board_color}\n")

    def show_saved_games(self):
        self.root.withdraw()  # Hide the Game Screen
        list_of_games_window = tk.Toplevel(self.root)
        list_of_games_window.title("List of Games Screen")
        list_of_games_screen = ListOfGamesScreen(list_of_games_window, self.player_name)

    def set_board_color(self, color):
        self.board_color = color
        self.root.configure(bg=self.board_color)

    def change_board_color(self):
        color = simpledialog.askstring("Change Board Color", "Enter a color name:")
        if color:
            self.set_board_color(color)

    def return_to_main(self):
        self.root.destroy()  # Close the Game Screen
        app.deiconify()  # Show the main window

    def close_program(self):
        app.destroy()  # Close the entire application

    def clear_active_game(self):
        try:
            with open("active_game.txt", "w") as file:
                file.write("")  # Clear the active game file
        except FileNotFoundError:
            pass

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Screen")

        # Display welcome message
        welcome_label = tk.Label(self.root, text="Welcome to TicTacToe Game!", font=("Helvetica", 16))
        welcome_label.pack(pady=20)

        self.player_name = simpledialog.askstring("Player Name", "Enter your name:")
        if not self.player_name:
            self.root.destroy()  # Close the application if the user doesn't enter a name

        self.create_game_button = tk.Button(self.root, text="Create Game", command=self.create_game)
        self.create_game_button.pack(pady=10)

        self.list_of_games_button = tk.Button(self.root, text="List of Games", command=self.list_of_games)
        self.list_of_games_button.pack(pady=10)

        self.change_name_button = tk.Button(self.root, text="Change Name", command=self.change_name)
        self.change_name_button.pack(pady=10)

        self.close_program_button = tk.Button(self.root, text="Close Program", command=self.close_program)
        self.close_program_button.pack(pady=10)

    def create_game(self):
        self.root.withdraw()  # Hide the main window
        game_window = tk.Toplevel(self.root)
        game_window.title("Game Screen")
        game_screen = GameScreen(game_window, self.player_name)

    def list_of_games(self):
        self.root.withdraw()  # Hide the main window
        list_of_games_window = tk.Toplevel(self.root)
        list_of_games_window.title("List of Games Screen")
        list_of_games_screen = ListOfGamesScreen(list_of_games_window, self.player_name)

    def change_name(self):
        new_name = simpledialog.askstring("Change Name", "Enter your new name:")
        if new_name:
            self.player_name = new_name

    def close_program(self):
        app.destroy()  # Close the entire application

if __name__ == "__main__":
    app = SingletonApp()
    MainApplication(app)
    app.mainloop()
