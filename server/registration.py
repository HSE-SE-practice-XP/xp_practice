import pygame

WIDTH, HEIGHT = 1000, 500
pygame.init()

window_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Регистрация")
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#000000'))

done = False

button_font = pygame.font.SysFont('Verdana', 15) # используем шрифт Verdana
button_text_color = pygame.Color("white")
button_color = pygame.Color("gray")
button_rect = pygame.Rect(100, 115, 100, 50)
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
    pygame.display.update()

    pygame.display.flip()