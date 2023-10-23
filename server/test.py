import unittest
from server import throw_dice
from server import get_result


class TestThrowDice(unittest.TestCase):

    def test_throw_dices(self):
        result = throw_dice()
        for i in result:
            assert 7 > i > 0


class TestGetResult(unittest.TestCase):

    def test_get_result(self):
        numbers = [2, 2, 2, 3, 1]
        result = get_result(numbers)
        self.assertEqual(result, 0)

        numbers = [2, 2, 2, 2, 1]
        result = get_result(numbers)
        self.assertEqual(result, 2)

        numbers = [4, 4, 4, 4, 4]
        result = get_result(numbers)
        self.assertEqual(result, 8)

        numbers = [4, 4, 1, 3, 6]
        result = get_result(numbers)
        self.assertEqual(result, -2)

        numbers = [4, 4, 6, 6, 5]
        result = get_result(numbers)
        self.assertEqual(result, -4)


class TestThrowAgain(unittest.TestCase):

    def test_throw_again(self):
        numbers = [1, 2, 3, 4, 5]
        indexes = [0, 3]
        new_numbers = throw_again(numbers, indexes)
        for i in new_numbers:
            assert 7 > i > 0


if __name__ == '__main__':
    unittest.main()

