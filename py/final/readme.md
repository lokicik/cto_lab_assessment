Main Screen:

* Displays a welcome message, prompting the user to enter their name.
Offers buttons for creating a new game, viewing a list of saved games, changing the player's name, and closing the program.

Game Create Screen: (doesn't work properly right now)

* Appears when the user chooses to create a new game.
Checks if there is an active game and displays information about it, allowing the user to continue the existing game or start a new one.
Provides a button to either continue the game or create a new one.


List of Games Screen:

* Displays a list of saved games filtered by the current player's name.
Allows the user to return to the main menu using a dedicated button.


Game Screen:

* Represents the actual Tic Tac Toe game.
Supports a 4x4 grid with buttons representing the game board.
Allows the player to make moves, and the computer makes moves for the opponent.
Includes buttons for viewing saved games, changing the board color, returning to the main menu, and closing the program.
Saves game results, including timestamps, player names, and board colors, to a file (game_results.txt).
The application maintains an active game state by saving relevant information to files (active_game.txt). Additionally, it handles user interactions, such as creating new games, viewing saved games, changing player names, and closing the program.