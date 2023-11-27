import pygame

WIDTH, HEIGHT = 1000, 500
pygame.init()

window_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Регистрация")
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#FFFFFF'))

# надпись
font = pygame.font.SysFont("Verdana", 25)
text = font.render(f"Введите количество и имена игроков:", True, "black")
players_cnt = font.render(f"Количество игроков: ", True, "black")
player1_text = font.render(f"Игрок 1: ", True, "black")
player2_text = font.render(f"Игрок 2: ", True, "black")
player3_text = font.render(f"Игрок 3: ", True, "black")
player4_text = font.render(f"Игрок 4: ", True, "black")
player5_text = font.render(f"Игрок 5: ", True, "black")


done = False

# кнопка старта
button_font = pygame.font.SysFont('Verdana', 15)  # используем шрифт Verdana
button_text_color = pygame.Color("black")
button_color = pygame.Color("gray")
button_rect = pygame.Rect(500, 300, 150, 70)
button_text = button_font.render('Начать игру', True, button_text_color)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # регистрируем пользователей
            done = True

    window_surface.blit(background, (0, 0))
    pygame.draw.rect(window_surface, button_color, button_rect)
    button_rect_center = button_text.get_rect(center=button_rect.center)
    window_surface.blit(button_text, button_rect_center)
    window_surface.blit(text, (10, 10))
    window_surface.blit(players_cnt, (10, 40))
    window_surface.blit(player1_text, (10, 70))
    window_surface.blit(player2_text, (10, 100))
    window_surface.blit(player3_text, (10, 130))
    window_surface.blit(player4_text, (10, 160))
    window_surface.blit(player5_text, (10, 190))

    pygame.display.update()

    pygame.display.flip()
