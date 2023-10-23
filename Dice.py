import pygame
class Dice:
    def __init__(self, x, y, n, key):
        self.die = None
        self.x = x
        self.y = y
        self.n = n
        selected = False

    def draw(self, screen):
        self.die = pygame.draw.rect(screen, (200, 200, 200), [self.x, self.y, 100, 100], 0, 5)
        pygame.image.load("dice_" + self.n + ".png")
        