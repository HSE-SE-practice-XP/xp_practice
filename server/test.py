import unittest
from server import Player


class TestThrowDice(unittest.TestCase):

    def test_throw_dices(self):
        result = Player.throw_dices()
        for i in result:
            assert 7 > i > 0


class TestGetResult(unittest.TestCase):

    def test_get_result(self):
        numbers = [2, 2, 2, 3, 1]
        player = Player("bob")
        player.numbers = numbers
        result = player.get_result_round_one()
        self.assertEqual(result, 0)

        numbers = [2, 2, 2, 2, 1]
        player.numbers = numbers
        result = player.get_result_round_one()
        self.assertEqual(result, 2)

        numbers = [4, 4, 4, 4, 4]
        player.numbers = numbers
        result = player.get_result_round_one()
        self.assertEqual(result, 8)

        numbers = [4, 4, 1, 3, 6]
        player.numbers = numbers
        result = player.get_result_round_one()
        self.assertEqual(result, -2)

        numbers = [4, 4, 6, 6, 5]
        player.numbers = numbers
        result = player.get_result_round_one()
        self.assertEqual(result, -4)


class TestThrowAgain(unittest.TestCase):

    def test_throw_again(self):
        numbers = [1, 2, 3, 4, 5]
        indexes = [0, 3]
        player = Player("bob")
        player.numbers = numbers
        new_numbers = player.throw_again(indexes)
        for i in new_numbers:
            assert 7 > i > 0


if __name__ == '__main__':
    unittest.main()

