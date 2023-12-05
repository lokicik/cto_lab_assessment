class GameManager:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def display_games(self):
        for game in self.games:
            print(f"Name: {game.name}, Status: {game.status}")

class Game:
    def __init__(self, name):
        self.name = name
        self.status = "Active"