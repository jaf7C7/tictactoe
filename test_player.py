from unittest import TestCase
from player import Player


class TestPlayer(TestCase):

    def test_is_human(self):
        human = Player(is_human=True)
        computer = Player(is_human=False)
        self.assertTrue(human.is_human)
        self.assertFalse(computer.is_human)

    def test_is_human_if_not_human(self):
        player = Player(is_human=False)
        self.assertFalse(player.is_human)
