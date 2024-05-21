from unittest import TestCase
from board import Board


class TestBoard(TestCase):

    def setUp(self):
        self.board = Board()

    def test_has_nine_positions(self):
        self.assertTrue(9, len(self.board.positions))

    def test_place_marker(self):
        self.board.place_marker('X', 3)
        self.assertEqual('X', self.board.positions[2])
