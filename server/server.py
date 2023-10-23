import random

import numpy as np


def throw_dice():
    result = []
    for i in range(5):
        random_number = random.randint(1, 6)
        result.append(random_number)
    return result


def throw_again(numbers: np.array, indexes: np.array):
    for index in indexes:
        random_number = random.randint(1, 6)
        numbers[index] = random_number


def get_result(numbers: np.array):
    best_num = 0
    max_count = 0
    for i in range(1, 7):
        count = 0
        for num in numbers:
            if num == i:
                count += 1
        if count >= max_count:
            best_num = i
            max_count = count
    return (max_count - 3) * best_num
