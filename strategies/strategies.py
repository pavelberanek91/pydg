'''
Name:
    strategies

Description:
    lorem
    Module node is used for creating graphs with oriented edges. Nodes can hold any data (even other objects).

Classes:
    Strategy
    AlwaysCooperate
    AlwaysDefect
    Random
    TitForTat
    TitForTwoTats

Functions:
    version(None) -> None
    help(Callable | type) -> None

Misc variables:
    __version__
'''


__version__ = "0.0.1"

from abc import ABC, abstractmethod
import random

class Strategy(ABC):
    '''
    lorem
    '''
    def __init__(self):
        self._game_history = []

    @property
    def game_history(self):
        return self._game_history

    @game_history.setter
    def game_history(self, value):
        self._game_history = value

    @abstractmethod
    def play(self):
        ...


class AlwaysCooperate(Strategy):
    '''
    lorem
    '''
    def play(self):
        return 'cooperate'


class AlwaysDefect(Strategy):
    '''
    lorem
    '''
    def play(self):
        return 'defect'


class Random(Strategy):
    '''
    lorem
    '''
    def play(self):
        return random.choice(['cooperate', 'defect'])


class TitForTat(Strategy):
    '''
    lorem
    '''
    def play(self):
        if self._game_history:
            last_game = self._game_history[-1]
            this, other = last_game
            return other
        else:
            return 'cooperate'
    

class TitForTwoTats(Strategy):
    '''
    lorem
    '''
    def play(self):
        if self._game_history:
            last_two_games = self._game_history[-2:-1]
            this = [game[0] for game in last_two_games]
            other = [game[1] for game in last_two_games]
            return 'defect' if all([decision == 'defect' for decision in other]) else 'cooperate'


#TODO:
#[ ] "grudger"
#[ ] "detective"
#[ ] "simplemind"

#FIXME:
# [ ]

#HACK:
# [ ]

#BUG:
# [ ] 

#XXX:
# [ ] is it possible or useful to use design pattern composit?