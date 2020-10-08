# Python Standard
from unittest import TestCase

# Local
from game_of_life import GameOfLife


class BaseTestClass(TestCase):
    def setUp(self) -> None:
        self.gol = GameOfLife(40)
        self.gol.set_initial_state([[1,0],[1,2],[1,3],[2,1]])


class PositionalTests(BaseTestClass):

    def test_get_top_left(self):
        print(self.gol.get_top_left([1,2]))

