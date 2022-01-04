# Problem: Write an implementation of a game score board given the below conditions
# 1. Each entry in the scoreboard will contain the player name and the score
# 2. The number of entry in the score board and game name will be decided by the driver program
# 3. A new record is only added to the scoreboard only if there is enough space or the score is atleast greater than the last score in the scoreboard
# 4. The scores in the score board is sorted in increasing order
# Author: Diamond Mohanty
# Date: 04-Jan-2022

class ScoreBoardEntry():
    def __init__(self, name: str, score: int) -> None:
        self._name: str = name
        self._score: int = score
    
    def get_name(self) -> str:
        return self._name

    def get_score(self) -> int:
        return self._score


class Scoreboard():
    def __init__(self, size: int, name: str) -> None:
        self._name:str = name
        self._scores: list[ScoreBoardEntry] = [None] * size
        self._entries = 0
    
    def add(self, entry: ScoreBoardEntry) -> None:
        """Adds a new score board entry

        Args:
            entry (ScoreBoardEntry): Score board entry instance
        """

        score = entry.get_score()
        if self._entries < len(self._scores) or score > self._scores[self._entries - 1].get_score():
            # Valid high score
            if self._entries < len(self._scores):
                self._entries += 1

            # Adding the entry in sorted order
            k = self._entries - 1

            # Right shift to make space
            while k > 0 and self._scores[k - 1].get_score() < score:
                self._scores[k] = self._scores[k - 1]
                k -= 1
            
            self._scores[k] = entry

    def show(self):
        for idx in range(self._entries):
            score = self._scores[idx]
            print("{0} scored {1} ".format(score.get_name(), score.get_score()))


# Test code
s1 = ScoreBoardEntry('Player 1', 740)
s2 = ScoreBoardEntry('Player 2', 710)
s3 = ScoreBoardEntry('Player 3', 750)
s4 = ScoreBoardEntry('Player 4', 610)
s5 = ScoreBoardEntry('Player 5', 700)
s6 = ScoreBoardEntry('Player 6', 630)
s7 = ScoreBoardEntry('Player 7', 400)

sb = Scoreboard(5, 'Hand Ball')
sb.add(s1)
sb.add(s2)
sb.add(s3)
sb.add(s4)
sb.add(s5)
sb.add(s6)
sb.add(s7)

sb.show()