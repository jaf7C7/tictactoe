from unittest import TestCase
from board import Board


class TestBoard(TestCase):

    def setUp(self):
        self.board = Board()

    def test_has_nine_positions(self):
        self.assertTrue(9, len(self.board.positions))

    def test_place_marker_marks_correct_position(self):
        self.board.place_marker('X', 3)
        self.assertEqual('X', self.board.positions[2])

    def test_winning_marker_if_winner(self):
        for positions in (
            [
                'X', 'X', 'X',
                4, 5, 6,
                7, 8, 9,
            ],
            [
                1, 2, 3,
                'X', 'X', 'X',
                7, 8, 9,
            ],
            [
                1, 2, 3,
                4, 5, 6,
                'X', 'X', 'X',
            ],
            [
                'X', 2, 3,
                'X', 5, 6,
                'X', 8, 9,
            ],
            [
                1, 'X', 3,
                4, 'X', 6,
                7, 'X', 9,
            ],
            [
                1, 2, 'X',
                4, 5, 'X',
                7, 8, 'X',
            ],
            [
                'X', 2, 3,
                4, 'X', 6,
                7, 8, 'X',
            ],
            [
                1, 2, 'X',
                4, 'X', 6,
                'X', 8, 9,
            ]
        ):
            self.board.positions = positions
            self.assertEqual(
                'X', self.board.winning_marker(), msg=self.board.positions
            )

    def test_winning_marker_if_no_winner(self):
        self.board.positions = [
            1, 2, 3,
            4, 5, 6,
            'X', 'X', 'O',
        ]
        self.assertIs(None, self.board.winning_marker())

    def test_is_full_if_full_board(self):
        self.board.positions = [
            'O', 'O', 'X',
            'X', 'X', 'O',
            'O', 'O', 'X',
        ]
        self.assertTrue(self.board.is_full())

    def test_is_full_if_not_full_board(self):
        self.board.positions = [
            'O', 'O', 'X',
            4, 'X', 'O',
            'O', 'O', 'X',
        ]
        self.assertFalse(self.board.is_full())
