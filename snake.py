import pygame
import random
from pygame.locals import*

def aleatorio():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x // 10 * 10, y // 10 * 10)

def colisao(c1,c2):
    if c1[0] == c2[0] and c1[1] == c2[1]:
        placar.pontos +=1
        return (c1[0] == c2[0] and c1[1] == c2[1])

def colide_parede(snake):
    return (snake[0] < 0 or snake[0] >= SCREEN_WIDHT or snake[1] < 0 or snake[1] > SCREEN_HEIGHT)

class Placar:
    def __init__(self):
        pygame.font.init()
        self.fonte=pygame.font.Font(None, 30)
        self.pontos = 0

    def contagem(self):
        self.text = self.fonte.render("Pontuação = " + str(self.pontos),1,(255,255,255))
        self.textpos = self.text.get_rect()
        self.textpos.centerx = screen.get_width()/6
        screen.blit(self.text,self.textpos)
        screen.blit(screen,(0,0))
BLACK = 0,0,0
WHITE = 255,255,255
END = False
SCREEN_WIDHT = 600
SCREEN_HEIGHT = 600

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
time = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDHT,SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill(WHITE)
my_direction = LEFT

apple_pos = aleatorio()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

placar = Placar()

while not END:
    time.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT

    if colisao(snake[0],apple_pos):
        apple_pos = aleatorio()
        snake.append((0,0))
    if colide_parede(snake[0]):
        pygame.quit()
    if my_direction == UP:
        snake[0] = (snake[0][0],snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0],snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10,snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10,snake[0][1])

    for i in range(len(snake)-1,0,-1):
        snake[i] = (snake[i-1][0],snake[i-1][1])
    

    screen.fill(BLACK)
    screen.blit(apple,apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)
    placar.contagem()
    pygame.display.update()