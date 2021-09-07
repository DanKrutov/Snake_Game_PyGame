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
        #if mixuruca pra evitar cores específicas, pouco efetivo
        if r != 255 and g != 255 and b != 255:
            a = 2
            return r, g, b

# sistema explosivo muito soda (incompleto WIP)
def explode():
    if portalização != 1:
        screen.fill((255, 0, 0))

#sistema inversor de direção pros portal(ou não)
def inversor():
    global my_direction
    if my_direction == UP:
        my_direction = DOWN
    elif my_direction == DOWN:
        my_direction = UP
    elif my_direction == RIGHT:
        my_direction = LEFT
    elif my_direction == LEFT:
        my_direction = RIGHT

# sistema que reseta o jogo
def resetador():
    if portalização != 1:
        global snake, ponto, speed, apple_pos, portal_pos, barrier_pos, my_direction
        apple_pos = on_grid_random()
        my_direction = LEFT
        portal_pos = [(on_grid_random()), (on_grid_random())]
        barrier_pos = [(on_grid_random()), on_grid_random(), on_grid_random(), on_grid_random(), on_grid_random()]
        snake = [(200, 200), (210, 200), (220, 200)]
        ponto = 0
        speed = 10

# função que define uma coordenada aleatória
def on_grid_random():
    x = random.randint(40, 610)
    y = random.randint(70, 640)
    # retorna os valores para que possam ser usados no jogo,
    # e para ficarem precisos em relação ao grid são multiplicados por 10
    return x // 10 * 10, y // 10 * 10

# sistema de colisão
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

# divisória
wall_pos = (20, 50)
wall_skin = pygame.Surface((620, 620))
wall_skin.fill((255, 255, 255))

# jooj
jooj_pos = (on_grid_random())
jooj_skin = pygame.Surface((10, 10))
jooj_skin.fill((255, 255, 0))

# fundo
gamescreen_pos = (30, 60)
gamescreen_skin = pygame.Surface((600, 600))
gamescreen_skin.fill((0, 0, 0))

# portais verdes
portal_pos = [(on_grid_random()), (on_grid_random())]
portal_skin = pygame.Surface((10, 10))
portal_skin.fill((0, 255, 0))

# portal da esquerda
portalE_pos = [(20, 340),(20, 350), (20, 360), (20, 370), (20, 380), (20, 390)]
# portal da direita
portalD_pos = [(630, 340),(630, 350), (630, 360), (630, 370), (630, 380), (630, 390)]
# cor dos portais fixos
portals_skin = pygame.Surface((10, 10))
portals_skin.fill((0, 0, 0))

# barreiras
barrier_pos = [(on_grid_random()), on_grid_random(), on_grid_random(), on_grid_random(), on_grid_random()]
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
cor = cor2 = (255, 255, 0)
clock = pygame.time.Clock()
escolha = 0
portalização = 0
# pontuação padrão
ponto = 0

jogo_ativo = 1
while jogo_ativo == 1:
    # Taxa de atualização do jogo, o padrão é 20 clocks por segundo
    clock.tick(speed)
    portalização = 0
    # placar de status
    size_font = font.render("tamanho: {tamanho} blocos".format(tamanho=len(snake)), True, cor)
    size_rect = size_font.get_rect()
    size_rect.topleft = (50, 10)
    score_font = font.render("{ponto} pontos".format(ponto=ponto), True, cor2)
    score_rect = score_font.get_rect()
    score_rect.topleft = (275, 10)
    vel_font = font.render("velocidade: {clock}x".format(clock=speed-9), True, cor)
    vel_rect = vel_font.get_rect()
    vel_rect.topleft = (475, 10)

    # cor do fundo(padrão 0,0,0 preto)
    screen.fill((0, 0, 0))
    gamescreen_skin.fill((0, 0, 0))

    # controles do jogo
    for event in pygame.event.get():
        # input para que ao apertar o "X" o jogo feche
        if event.type == QUIT:
            print("Você fechou o jogo!")
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
            if event.key == K_x:
                apple.fill((255, 0, 0))
            if event.key == K_ESCAPE:
                print("Você fechou o jogo!")
                pygame.quit()

    # ações após colisão entre a maçã e a cobra:
    if collision(snake[0], apple_pos):
        # é gerado novo spawn pra maçã
        apple_pos = on_grid_random()
        # piscada maneira
        screen.fill(randomcolor())
        # um novo quadrado pra cobra, aumentando seu tamanho
        snake.append((0, 0))
        barrier_pos.append(on_grid_random())
        jooj_pos = (on_grid_random())
        # as barreiras são atualizadas!
        portal_pos = [(on_grid_random()), (on_grid_random())]
        barrier_pos = [(on_grid_random()), on_grid_random(), on_grid_random(), on_grid_random(), on_grid_random()]
        # aumentado a pontuação
        ponto = ponto + 1
        # sistema que decide se o jooj vai aparecer ou não na próxima randomização!
        if ponto > 5:
            escolha = random.randint(0, 4)
            if ponto == 1:
                print("jooj ativado!")

        # aumentado a velocidade
        if speed < 15:
            speed = speed + 1
        elif speed >= 15 and speed <20:
            speed = speed + 0.5
        elif speed >= 20:
            speed = speed + 0.25

    # impede que a maçã e as barreiras fiquem na mesma coord
    if apple_pos == barrier_pos:
        apple_pos = on_grid_random()

    # impede que o portais e as barreiras fiquem na mesma coord
    if portal_pos[0] == barrier_pos:
        portal_pos[0] = on_grid_random()
    if portal_pos[1] == barrier_pos:
        portal_pos[1] = on_grid_random()

    # impede que os portais e a maçã fiquem na mesma coord
    if portal_pos == apple_pos:
        apple_pos = on_grid_random()

    # efeito colorido na cobra
    snake_skin.fill(randomcolor())

    # efeito no placar caso atingido uma pontuação especifica
    if ponto == 5 or ponto == 10 or ponto == 15 or ponto == 20 or ponto == 25 or ponto == 30 or ponto == 35 or ponto == 40:
        cor2 = randomcolor()
    else:
        cor2 = 255, 255, 0

    # sistema de colisão entre a cobra e as barreiras(versão lenght enhanced :D)
    for i in range(0, len(barrier_pos)):
        if snake[0][0] == barrier_pos[i][0] and snake[0][1] == barrier_pos[i][1]:
            speed = 1
            gamescreen_skin.fill((255, 0, 0))
            resetador()

    # sistema de colisão dos portais fixos (sim ficou esse código gigante pq nn sei generalizar lista >:( )
    # portal direita
    if collision(snake[0], portalD_pos[0]) or collision(snake[0], portalD_pos[1]) or collision(snake[0],portalD_pos[2]) or collision(snake[0], portalD_pos[3]) or collision(snake[0], portalD_pos[4]) or collision(snake[0], portalD_pos[5]):
        for i in range(0, len(portalD_pos)):
            if snake[0][0] == portalD_pos[i][0] and snake[0][1] == portalD_pos[i][1]:
                portalização = 1
                snake[0] = portalE_pos[random.randint(0, 5)]
                screen.fill((0, 255, 0))
    #portal esquerda
    elif collision(snake[0], portalE_pos[0]) or collision(snake[0], portalE_pos[1]) or collision(snake[0], portalE_pos[2]) or collision(snake[0], portalE_pos[3]) or collision(snake[0], portalE_pos[4]) or collision(snake[0], portalE_pos[5]):
        for i in range(0, len(portalE_pos)):
            if snake[0][0] == portalE_pos[i][0] and snake[0][1] == portalE_pos[i][1]:
                portalização = 1
                snake[0] = portalD_pos[random.randint(0,5)]
                screen.fill((0, 255, 0))

    # sistema de colisão sobre o próprio corpo
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            print("Morte: bateu em si mesmo")
            speed = 1
            gamescreen_skin.fill((255, 0, 0))
            resetador()
            break

    # colisão com o jooj
    if collision(snake[0], jooj_pos) and escolha == 1:
        escolha = 0
        if speed >= 10:
            speed = speed - 2
        elif speed <10:
            speed = speed - 1

    # sistema de teleporte super avançado
    if collision(snake[0], portal_pos[0]):
        snake[0] = portal_pos[1]
        inversor()
    elif collision(snake[0], portal_pos[1]):
        snake[0] = portal_pos[0]
        inversor()

    # sistema onde o jogador perde caso saia da área permitida
    if snake[0][0] >= 630 or snake[0][1] >= 660 or snake[0][0] < 30 or snake[0][1] < 60:
        resetador()

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
    screen.blit(apple, apple_pos)
    screen.blit(score_font, score_rect)
    screen.blit(vel_font, vel_rect)
    screen.blit(size_font, size_rect)
    if escolha == 1:
        screen.blit(jooj_skin, jooj_pos)
    for pos4 in portalD_pos:
        screen.blit(portals_skin, pos4)
    for pos3 in portalE_pos:
        screen.blit(portals_skin, pos3)
    for pos2 in portal_pos:
        screen.blit(portal_skin, pos2)
    for pos1 in barrier_pos:
        screen.blit(barrier_skin, pos1)
    for pos in snake:
        screen.blit(snake_skin, pos)

    # função que fazerá a tela do jogo atualizar após o final de cada clock(ou while)
    pygame.display.update()
