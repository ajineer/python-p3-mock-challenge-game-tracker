class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
        

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and title and not hasattr(self, 'title'):
            self._title = title 
        else:
            raise ValueError("Cannot change title or title must be a string with length greater than 0.")

    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players
    
    def average_score(self, player):
        scores = [r.score for r in self._results if r.player == player]
        return sum(scores)/len(scores) if scores else None