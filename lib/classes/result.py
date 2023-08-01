from classes.game import Game

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        game.results(self)
        game.players(player)
        player.results(self)
        player.games_played(game)
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if not isinstance(value, int) or not 1 <= value <= 5000:
            raise ValueError("score must be int between 1 and 5000")
        else:
            self._score = value

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game_instance):
        if not isinstance(game_instance, Game):
            raise ValueError("game must be instance of Game class")
        else:
            self._game = game_instance