from unittest import TestCase
from board import Board


class TestBoard(TestCase):

    def setUp(self):
        self.board = Board()

    def test_has_nine_positions(self):
        self.assertTrue(9, len(self.board.positions))
