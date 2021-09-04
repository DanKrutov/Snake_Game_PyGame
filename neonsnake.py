import pygame
import random
from pygame.locals import *

# cor aleatória
def randomcolor():
    a = 1
    while a == 1:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        #if mixuruca pra evitar cores específicas, pouco efetivo :(
        if r != 255 and g != 255 and b != 255:
            a = 2
            return r, g, b

# função que define uma coordenada aleatória
def on_grid_random():
    x = random.randint(40, 610)
    y = random.randint(70, 640)
    # retorna os valores para que possam ser usados no jogo,
    # e para ficarem precisos em relação ao grid são multiplicados por 10
    return x // 10 * 10, y // 10 * 10

# funçao pra colisão
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
# tamanho da tela(600x600)
screen = pygame.display.set_mode((660, 690))
# nome que irá aparecer na janela
pygame.display.set_caption('NeonSnake')

# fonte definida pro placar(não ta funcionando lol)
font = myfont = pygame.font.SysFont("PressStart2P.tff",25)
ponto = 0

# divisória
wall_pos = (20, 50)
wall_skin = pygame.Surface((620, 620))
wall_skin.fill((255, 255, 255))

# fundo do jooj
gamescreen_pos = (30, 60)
gamescreen_skin = pygame.Surface((600, 600))
gamescreen_skin.fill((0, 0, 0))

# portais
portal1_pos = (on_grid_random())
portal2_pos = (on_grid_random())
portal_skin = pygame.Surface((10, 10))
portal_skin.fill((0, 255, 0))

# barreiras
barrier1_pos = (on_grid_random())
barrier2_pos = (on_grid_random())
barrier3_pos = (on_grid_random())
barrier4_pos = (on_grid_random())
barrier5_pos = (on_grid_random())
barrier_skin = pygame.Surface((10, 10))
barrier_skin.fill((255, 255, 255))

# posição inicial do corpo da cobra constituente de 3 quadrados
snake = [(200, 200), (210, 200), (220, 200)]
# desenho da cobra, um quadrado 10x10
snake_skin = pygame.Surface((10, 10))


# declaração definindo que a maçã irá aparecer numa cordenada definida pela função de grid_random
apple_pos = on_grid_random()
# desenho da maçã, um quadrado 10x10
apple = pygame.Surface((10, 10))
# cor da maçã
apple.fill((255, 0, 0))

# direção padrão da cobra ao iniciar o jogo
my_direction = LEFT
# vel padrão
speed = 10
# cor padrão do placar
cor = 255, 255, 0
clock = pygame.time.Clock()

while True:
    # Taxa de atualização do jogo, o padrão é 20 clocks por segundo
    clock.tick(speed)

    # placar de pontuação e velocidade
    score_font = font.render("pontuação: {ponto}".format(ponto=ponto), True, cor)
    score_rect = score_font.get_rect()
    score_rect.topleft = (200, 10)
    vel_font = font.render("velocidade: {clock}x".format(clock=speed-9), True, cor)
    vel_rect = vel_font.get_rect()
    vel_rect.topleft = (350, 10)

    # cor do fundo(padrão 0,0,0 preto)
    screen.fill((0, 0, 0))
    gamescreen_skin.fill((0, 0, 0))

    # controles do jogo
    for event in pygame.event.get():
        # input para que ao apertar o "X" o jogo feche
        if event.type == QUIT:
            pygame.quit()

        # Controles de direçao
        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
            if event.key == K_ESCAPE:
                pygame.quit()

    # ações após colisão entre a maçã e a cobra:
    if collision(snake[0], apple_pos):
        # é gerado novo spawn pra maçã
        apple_pos = on_grid_random()
        # piscada maneira
        screen.fill(randomcolor())
        # um novo quadrado pra cobra, aumentando seu tamanho
        snake.append((0, 0))
        # as barreiras são atualizadas!
        portal1_pos = on_grid_random()
        portal2_pos = on_grid_random()
        barrier1_pos = on_grid_random()
        barrier2_pos = on_grid_random()
        barrier3_pos = on_grid_random()
        barrier4_pos = on_grid_random()
        barrier5_pos = on_grid_random()
        # aumentado a pontuação
        ponto = ponto + 1
        # aumentado a velocidade
        if speed < 15:
            speed = speed + 1
        elif speed >= 15 and speed <20:
            speed = speed + 0.5
        elif speed >= 20:
            speed = speed + 0.25

    # impede que a maçã e as barreiras fiquem na mesma coord
    if apple_pos == barrier1_pos or apple_pos == barrier2_pos or apple_pos == barrier3_pos or apple_pos == barrier4_pos or apple_pos == barrier5_pos:
        apple_pos = on_grid_random()
    # impede que o portais e as barreiras fiquem na mesma coord
    if portal1_pos == barrier1_pos or portal1_pos == barrier2_pos or portal1_pos == barrier3_pos or portal1_pos == barrier4_pos or portal1_pos == barrier5_pos:
        portal1_pos = on_grid_random()
    if portal2_pos == barrier1_pos or portal2_pos == barrier2_pos or portal2_pos == barrier3_pos or portal2_pos == barrier4_pos or portal2_pos == barrier5_pos:
        portal2_pos = on_grid_random()
    # impede que os portais e a maçã fiquem na mesma coord
    if portal1_pos == apple_pos or portal2_pos == apple_pos:
        apple_pos = on_grid_random()

    # efeito colorido na cobra
    snake_skin.fill(randomcolor())

    # o jogador perde se tocar nas barreiras
    if collision(snake[0], barrier1_pos) or collision(snake[0], barrier2_pos) or collision(snake[0], barrier3_pos) or collision(snake[0], barrier4_pos) or collision(snake[0], barrier5_pos):
        pygame.quit()

    # sistema de colisão sobre o próprio corpo
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            pygame.quit()

    # sistema de teleporte super avançado
    if collision(snake[0], portal1_pos):
        snake[0] = portal2_pos
        if my_direction == UP:
            my_direction = DOWN
        elif my_direction == DOWN:
            my_direction = UP
        elif my_direction == RIGHT:
            my_direction = LEFT
        elif my_direction == LEFT:
            my_direction = RIGHT
    elif collision(snake[0], portal2_pos):
        snake[0] = portal1_pos
        if my_direction == UP:
            my_direction = DOWN
        elif my_direction == DOWN:
            my_direction = UP
        elif my_direction == RIGHT:
            my_direction = LEFT
        elif my_direction == LEFT:
            my_direction = RIGHT

    # sistema onde o jogador perde caso saia da área permitida
    if snake[0][0] >= 630 or snake[0][1] >= 660 or snake[0][0] < 30 or snake[0][1] < 60:
        pygame.quit()

    # sistema que faz o corpo da cobra seguir sua cabeça
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    # Movimemento da cobra, de acordo com a direção escolhida pelo input
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    # aparentemente, fazem os elementos serem desenhados em todos os clocks
    screen.blit(wall_skin, wall_pos)
    screen.blit(gamescreen_skin, gamescreen_pos)
    screen.blit(portal_skin, portal1_pos)
    screen.blit(portal_skin, portal2_pos)
    screen.blit(apple, apple_pos)
    screen.blit(barrier_skin, barrier1_pos)
    screen.blit(barrier_skin, barrier2_pos)
    screen.blit(barrier_skin, barrier3_pos)
    screen.blit(barrier_skin, barrier4_pos)
    screen.blit(barrier_skin, barrier5_pos)
    screen.blit(score_font, score_rect)
    screen.blit(vel_font, vel_rect)

    for pos in snake:
        screen.blit(snake_skin, pos)

    # função que fazerá a tela do jogo atualizar após o final de cada clock(ou while)
    pygame.display.update()
