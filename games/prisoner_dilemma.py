'''
Name:
    prisoner_dilemma

Description:
    lorem
    Module node is used for creating graphs with oriented edges. Nodes can hold any data (even other objects).

Classes:
    Game

Functions:
    version(None) -> None
    help(Callable | type) -> None

Misc variables:
    __version__
'''


__version__ = "0.0.1"


from abc import ABC


class Game(ABC):

    def __init__(self, payoffMatrix: list):
        self._payoffMatrix = payoffMatrix

    @property
    def payoffMatrix(self) -> list:
        return self._payoffMatrix

    @payoffMatrix.setter
    def payoffMatrix(self, value: list) -> None:
        self._payoffMatrix = value