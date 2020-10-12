# Python Standard
from unittest import TestCase

# Local
from game_of_life import GameOfLife


class BaseTestClass(TestCase):
    def setUp(self) -> None:
        self.gol = GameOfLife(40)
        self.gol.set_initial_state([[1,0],[1,1],[0,1],[0,2],[0,3],[1,2],[1,3],[2,1]])


class PositionalTests(BaseTestClass):

    def test_get_top_left(self):
        self.assertEqual(self.gol.get_top_left([1,2]),1)

    def test_get_top_center(self):
        self.assertEqual(self.gol.get_top_center([1,2]),1)

    def test_get_top_right(self):
        self.assertEqual(self.gol.get_top_right([1,2]),1)

    def test_get_center_left(self):
        self.assertEqual(self.gol.get_center_left([1,2]),1)

    def test_get_center_right(self):
        self.assertEqual(self.gol.get_center_right([1,2]),1)

    def test_get_bottom_left(self):
        self.assertEqual(self.gol.get_bottom_left([1,2]),1)

    def test_get_bottom_center(self):
        self.assertEqual(self.gol.get_bottom_center([1,2]),0)

    def test_get_bottom_right(self):
        self.assertEqual(self.gol.get_bottom_right([1,2]),0)

    def test_get_total_number_of_neighbours(self):
        self.assertEqual(self.gol.get_total_number_of_neighbours([1,2]),6)


class CellChangeTests(BaseTestClass):

    def test_dead_becomes_alive(self):
        self.assertFalse(self.gol.dead_becomes_alive([0,1]))

    def test_alive_remains_alive(self):
        self.assertTrue(self.gol.alive_remains_alive([1,3]))



