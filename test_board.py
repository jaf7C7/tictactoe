from unittest import TestCase
from board import Board


class TestBoard(TestCase):

    def setUp(self):
        self.board = Board()

    def test_has_positions(self):
        self.assertTrue(hasattr(self.board, 'positions'))
