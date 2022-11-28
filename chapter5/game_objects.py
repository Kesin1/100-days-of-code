from typing import List


class Roll:
    def __init__(self, name: str , defeating: List, defeated_by: List):
        "docstring"
        self.name = name
        self.defeating = defeating
        self.defeated_by = defeated_by

    def can_defeat(self, roll):
        if roll.name in self.defeating:
            return 'WON'
        elif self.name in roll.defeating:
            return 'LOSE'
        else:
            return 'TIE'

class Player:
    def __init__(self, name):
        "docstring"
        self.name = name
        self.wins = 0


