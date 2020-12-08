"""sds
Usando a biblioteca ‘pygame’, escreva um programa que desenha um botão (círculo) com o texto “clique” sobre ele na parte superior da tela. Quando o botão for clicado, ele deve chamar uma função que desenha um retângulo em uma posição aleatória na tela. Caso um retângulo apareça na mesma posição que um já existente, ambos devem ser eliminados.
"""

import pygame, random, math

pygame.init()
screen_width = 800
screen_height = 600

black = (0, 0, 0)
blue = (3, 44, 166)

list_of_squares = []    
squares_test = []

screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(black)
pygame.display.set_caption('Ex 09')

class Circle:
    def __init__(self):
        self.color = blue
        self.area = [screen_width // 2, screen_height // 4]
    
    def draw(self):
        pygame.draw.circle(screen, self.color, self.area, 100)
    
    def addText(self):
        font = pygame.font.SysFont("comicsansms", 18)
        text = font.render("Clique", 1, (255,255,255))
        textpos = text.get_rect(center=(self.area))
        screen.blit(text, textpos)

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

def check_square_position(square_object):
    square_object_area = square_object.area
    last_square_drawn = None

    for square in list_of_squares:
        if square_object_area.colliderect(square):
            last_square_drawn = square_object_area
            list_of_squares.remove(square)
            pygame.draw.rect(screen, black, square)
    
    list_of_squares.append(square_object_area)

    if last_square_drawn in list_of_squares:
        pygame.draw.rect(screen, black, last_square_drawn)
        list_of_squares.remove(last_square_drawn)
    
    pygame.display.update()

def checkSelection():
    positons = []
    mouse_x = 0
    mouse_y = 0
    for positon in pygame.mouse.get_pos():
        positons.append(positon)
    mouse_x = positons[0]
    mouse_y = positons[1]    
    positons.remove(mouse_x)
    positons.remove(mouse_y)

    a = (mouse_x - 400) ** 2
    b = (mouse_y - 150) ** 2

    if math.sqrt(a + b) < 100:
        square = Square()
        square.draw()
        check_square_position(square)
        
circle = Circle()

terminou = False
while not terminou:
    circle.draw()
    circle.addText()
    square = Square()
    
    # Checar os eventos do mouse aqui
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            checkSelection()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                circle.color = black
                circle.draw()
                circle.area[0] -= 10
                circle.color = blue
                circle.draw()
            if event.key == pygame.K_d:
                circle.color = black
                circle.draw()
                circle.area[0] += 10
                circle.color = blue
                circle.draw()
            if event.key == pygame.K_w:
                circle.color = black
                circle.draw()
                circle.area[1] -= 10
                circle.color = blue
                circle.draw()
            if event.key == pygame.K_s:
                circle.color = black
                circle.draw()
                circle.area[1] += 10
                circle.color = blue
                circle.draw()
        if event.type == pygame.QUIT:
            terminou = True

    pygame.display.update()

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()