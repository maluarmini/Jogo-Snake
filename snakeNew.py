import pygame
from pygame.locals import *
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#FUNÇÔES E CLASSES
def aleatorio():
    x = random.randint(0,790)
    y = random.randint(0,590)
    return x//10*10,y//10*10

def colide_apple(c1,c2):
    if (c1[0] == c2[0] and c1[1] == c2[1]):
        return True

def colide_parede(snake):
    if snake[0] < 0 or snake[0] > SCREEN_WIDTH - 10 or snake[1] < 0  or snake[1] > SCREEN_HEIGHT - 10:
        return True
class Placar:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(None,30)
        self.pts = 0

    def contagem(self):
        self.text = self.font.render(str(self.pts),1,(WHITE))
        self.text_pos = self.text.get_rect(center=(SCREEN_WIDTH/2,20))
        screen.blit(self.text,self.text_pos)

#CONFIGURAÇÔES DE TELA
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen_rect = screen.get_rect()
pygame.display.set_caption('Snake - PYGAME')
fps = pygame.time.Clock()

#SNAKE
snake = [(200,200),(210,200),(220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill(WHITE)
snake_direction  = -1

#APPLE
apple = pygame.Surface((10,10))
apple.fill(RED)
apple_pos = aleatorio()

#PLACAR
placar = Placar()

while True:
    fps.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                snake_direction = RIGHT
            if event.key == K_LEFT:
                snake_direction = LEFT
            if event.key == K_DOWN:
                snake_direction = DOWN
            if event.key == K_UP:
                snake_direction = UP
    #MOVIMENTAÇÂO DA COBRA
    if snake_direction == RIGHT:
        snake[0] = (snake[0][0] + 10,snake[0][1])
    if snake_direction == LEFT:
        snake[0] = (snake[0][0] - 10,snake[0][1])
    if snake_direction == UP:
        snake[0] = (snake[0][0],snake[0][1] - 10)
    if snake_direction == DOWN:
        snake[0] = (snake[0][0],snake[0][1] + 10)
    for i in range(len(snake) - 1,0,-1):
        snake[i] = (snake[i-1][0],snake[i-1][1])
    #COLISOES    
    if colide_apple(snake[0],apple_pos):
        apple_pos = aleatorio()
        snake.append((800,600))
        placar.pts += 1
    if colide_parede(snake[0]):
        pygame.quit()

    screen.fill(BLACK)
    for pos in snake:
        screen.blit(snake_skin,pos)
    screen.blit(apple,apple_pos)
    placar.contagem()

    pygame.display.update()