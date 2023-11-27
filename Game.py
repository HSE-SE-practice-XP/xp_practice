from server.server import Player
import pygame
import sys


class Game:
    def __init__(self, num):
        self.players = [Player() for _ in range(num)]
        self.queue = 0
        self.is_game_on = False
        self.n = num

    def ask_for_names(self):
        for i in range(self.n):
            # Запросить имя игрока
            name = ""
            self.players[i].set_name(name)

    def start(self):
        self.is_game_on = True

        pygame.init()

        # Установка размеров окна
        WIDTH, HEIGHT = 2000, 1000
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Игральные кубики")

        # Загрузка изображения кубика
        cube_image_1 = pygame.image.load('dices/dice_1.jpg')
        cube_image_2 = pygame.image.load('dices/dice_2.jpg')
        cube_image_3 = pygame.image.load('dices/dice_3.jpg')
        cube_image_4 = pygame.image.load('dices/dice_4.jpg')
        cube_image_5 = pygame.image.load('dices/dice_5.jpg')
        cube_image_6 = pygame.image.load('dices/dice_6.jpg')
        throw_image = pygame.image.load('dices/throw.jpg')

        # Создание прямоугольников для кнопок
        cube_rects = []

        for i in range(5):
            cube_rect = cube_image_2.get_rect()
            cube_rect.topleft = (200 * i + 50, 50)
            cube_rects.append(cube_rect)

        cube_rect_throw = throw_image.get_rect()
        cube_rect_throw.topleft = (500, 200)

        while self.is_game_on:
            # написать кто ходит на экране

            player = self.players[self.queue]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, rect in enumerate(cube_rects):
                        if rect.collidepoint(mouse_pos):
                            # Вызов вашей функции при нажатии на кнопку
                            print(f"Вы нажали на кубик {i + 1}")
                    if cube_rect_throw.collidepoint(mouse_pos):
                        player.throw_dices()
                    numbers = player.numbers
                    for i, j in enumerate(numbers):
                        if j == 1:
                            screen.blit(cube_image_1, cube_rects[0].move(200 * i, 0))
                        if j == 2:
                            screen.blit(cube_image_2, cube_rects[1].move(200 * i, 0))
                        if j == 3:
                            screen.blit(cube_image_3, cube_rects[2].move(200 * i, 0))
                        if j == 4:
                            screen.blit(cube_image_4, cube_rects[3].move(200 * i, 0))
                        if j == 5:
                            screen.blit(cube_image_5, cube_rects[4].move(200 * i, 0))
                        if j == 6:
                            screen.blit(cube_image_6, cube_rects[5].move(200 * i, 0))

            # Очистка экрана
            screen.fill((255, 255, 255))

            # Рисование изображений кубиков
            for i, rect in enumerate(cube_rects):
                screen.blit(cube_image_2, rect.move(200 * i, 0))
            screen.blit(throw_image, cube_rect_throw.move(500, 200))

            # Обновление экрана
            pygame.display.flip()


if __name__ == "__main__":
    num = 5 # получить количество игроков
    game = Game(num)
    game.ask_for_names()
    game.start()
