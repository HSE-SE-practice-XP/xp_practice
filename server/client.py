import pygame
import sys
import random
import time

import numpy as np

from server import Player

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WIDTH, HEIGHT = 2000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Покер на костях")

# Загрузка изображения кубика
cube_image_1 = pygame.image.load('server/dices/dice_1.jpg')
cube_image_2 = pygame.image.load('server/dices/dice_2.jpg')
cube_image_3 = pygame.image.load('server/dices/dice_3.jpg')
cube_image_4 = pygame.image.load('server/dices/dice_4.jpg')
cube_image_5 = pygame.image.load('server/dices/dice_5.jpg')
cube_image_6 = pygame.image.load('server/dices/dice_6.jpg')
throw_image = pygame.image.load('server/dices/throw.jpg')
const_cub = pygame.image.load('server/dices/const.jpg')


# Создание прямоугольников для кнопок
cube_rects = []

for i in range(6):
    cube_rect = cube_image_2.get_rect()
    cube_rect.topleft = (200 * i + 50, 50)
    cube_rects.append(cube_rect)

cube_rect_throw = throw_image.get_rect()
cube_rect_throw.topleft = (500, 200)

cube_rect_const = const_cub.get_rect()
cube_rect_const.topleft = (800, 200)

none_throw_cubes = np.array([2, 4])

def print_all_cub():

    for index, rect in enumerate(cube_rects):
        if index > 4:
            break
        if np.any(none_throw_cubes == index):
             screen.blit(const_cub, rect.move(200 * index, 300))
        i = random.randint(0, 5)
        if i == 0:
            screen.blit(cube_image_1, rect.move(200 * index, 0))
        if i == 1:
            screen.blit(cube_image_2, rect.move(200 * index, 0))
        if i == 2:
            screen.blit(cube_image_3, rect.move(200 * index, 0))
        if i == 3:
            screen.blit(cube_image_4, rect.move(200 * index, 0))
        if i == 4:
            screen.blit(cube_image_5, rect.move(200 * index, 0))
        if i == 5:
            screen.blit(cube_image_6, rect.move(200 * index, 0))

    screen.blit(throw_image, cube_rect_throw.move(500, 300))

    # Обновление экрана
    pygame.display.flip()

area_rect = pygame.Rect(1000, 500, 300, 75)  # (150, 150) - начальная точка, 50 - ширина и высота



throw_allowed = True


# Основной игровой цикл
running = True
while running:
    if throw_allowed:
        print_all_cub()
    throw_allowed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            '''throw_allowed = True'''
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if area_rect.collidepoint(mouse_x, mouse_y):
                throw_allowed = True
