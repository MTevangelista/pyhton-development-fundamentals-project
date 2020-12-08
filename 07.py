"""
Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta), toda vez que a tecla espaço for pressionada ou o botão direito for clicado.
"""

import pygame, random

pygame.init()
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

class Square:
    def __init__(self, side=50):
        self.side = side
        self.x, self.y = self.generate_random_position()
        self.color = (255, 255, 0)
        self.area = pygame.Rect(self.x, self.y, self.side, self.side)
    
    def generate_random_position(self):
        return (random.randint(0, screen_width - self.side), random.randint(0, screen_height - self.side))

    def draw(self):
        pygame.draw.rect(screen, self.color, self.area)

terminou = False
RIGHT = 3
while not terminou:
    square = Square()
    # Checar os eventos do mouse aqui
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                square.draw()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            square.draw()
        if event.type == pygame.QUIT:
            terminou = True
    pygame.display.update()

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()