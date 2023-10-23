import random

import numpy as np


class Player:
    def __init__(self, name):
        self.points = 0
        self.name = name
        self.numbers = [0 for _ in range(5)]

    def throw_dices(self):
        for i in range(5):
            random_number = random.randint(1, 6)
            self.numbers[i] = random_number
        return self.numbers

    def throw_again(self, indexes):
        for index in indexes:
            random_number = random.randint(1, 6)
            self.numbers[index] = random_number
        return self.numbers

    def get_result_round_one(self):
        best_points = -31
        for i in range(1, 7):
            count = 0
            for num in self.numbers:
                if num == i:
                    count += 1
            if count > 0:
                best_points = max(best_points, (count - 3) * i)
        self.points = best_points
        return best_points


class Play:
    def __init__(self, players_names):
        self.players = [Player(name) for name in players_names]

    def get_results(self):
        answer = []
        for player in self.players:
            answer.append(player.points)

