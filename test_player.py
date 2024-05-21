from unittest import TestCase
from player import Player


class TestPlayer(TestCase):

    def test_is_human_if_human(self):
        player = Player(is_human=True)
        self.assertTrue(player.is_human)

    def test_is_human_if_not_human(self):
        player = Player(is_human=False)
        self.assertFalse(player.is_human)
