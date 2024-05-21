from unittest import TestCase
from player import Player


class TestPlayer(TestCase):

    def test_is_human(self):
        human = Player(is_human=True)
        computer = Player(is_human=False)
        self.assertTrue(human.is_human)
        self.assertFalse(computer.is_human)

    def test_markers(self):
        human = Player(is_human=True)
        computer = Player(is_human=False)
        self.assertEqual('X', human.marker)
        self.assertEqual('O', computer.marker)
