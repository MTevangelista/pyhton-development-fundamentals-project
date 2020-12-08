import pygame, random

pygame.init()
screen_width = 600
screen_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((screen_width, screen_height))

def draw_square(x, y, width, height):
    pygame.draw.rect(screen, black, [x, y, width, height], 2)

def draw_circle(x, y, width, height):
    pygame.draw.ellipse(screen, black, [x, y, width, height], 2)

terminou = False
while not terminou:
    # Checar os eventos do mouse aqui
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    screen.fill(white)

    draw_square(30, 30, 535, 485)

    draw_square(50, 50, 200, 200)
    draw_square(50, 300, 200, 200)

    draw_circle(350, 50, 200, 200)
    draw_circle(350, 300, 200, 200)

    draw_square(60, 310, 80, 80)
    draw_circle(160, 310, 80, 80)
    draw_circle(160, 410, 80, 80)
    draw_square(60, 410, 80, 80)

    draw_square(65, 415, 30, 30)
    draw_circle(105, 415, 30, 30)
    draw_circle(105, 455, 30, 30)
    draw_square(65, 455, 30, 30)

    draw_square(68, 458, 10, 10)
    draw_circle(82, 458, 10, 10)
    draw_circle(82, 472, 10, 10)
    draw_square(68, 472, 10, 10)

    pygame.display.update()

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()
