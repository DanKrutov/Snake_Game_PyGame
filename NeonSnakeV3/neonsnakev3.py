import pygame
import sys, shelve
import random
from pygame.locals import *


# renderiza todos os elementos
def render(tb):
    screen.blit(wall_skin, wall_pos)
    screen.blit(gamescreen_skin, gamescreen_pos)
    screen.blit(apple, apple_pos)

    if tb == 0:
        screen.blit(score_font, score_rect)
        screen.blit(vel_font, vel_rect)
        screen.blit(size_font, size_rect)
        screen.blit(hs_font, hs_rect)

    if escolha == 1:
        screen.blit(jooj_skin, jooj_pos)
    for pos6 in portalB_pos:
        screen.blit(portals_skin, pos6)
    for pos5 in portalC_pos:
        screen.blit(portals_skin, pos5)
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


# cor aleatória
def randomcolor():
    a = 1
    while a == 1:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        # if mixuruca pra evitar cores específicas, pouco efetivo
        if r != 255 and g != 255 and b != 255:
            return r, g, b


# Interface de menu
def menu():
    global jogo_ativo

# pause daora
def pause():
    global jogo_ativo
    jogo_ativo = 0
    print("você pausou!")
    while jogo_ativo == 0:
        # pra fazer o "pause" piscar, nn ta funcionando ainda
        cor3 = 255, 255, 255
        if cor3 == (255,255,255):
            cor3 = (0, 0, 0)
        if cor3 == (0, 0, 0):
            cor3 = (255,255,255)

        pause_font = font2.render("PAUSE", True, cor3)
        pause_rect = pause_font.get_rect()
        pause_rect.midbottom = (660 / 2, 680 / 2)

        txt_font = font.render("Deseja Sair? (Y/N)", True, cor)
        txt_rect = txt_font.get_rect()
        txt_rect.midbottom = (660 / 2, 680 / 2 + 30)

        render(tb=1)
        screen.blit(pause_font, pause_rect)
        screen.blit(txt_font, txt_rect)
        pygame.display.update()

        # input do pause
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Você fechou o jogo")
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_n:
                    print("você despausou!")
                    jogo_ativo = 1
                if event.key == K_y:
                    pygame.quit()
                    sys.exit()


# sistema explosivo muito soda (incompleto WIP)
def explode():
    if portalizacao != 1:
        screen.fill((255, 0, 0))


# teleporte dos portais fixos!!!!
def portfixo(portalA, portalB):
    global snake, portalizacao
    for i in range(0, len(portalA)):
        if snake[0][0] == portalA[i][0] and snake[0][1] == portalA[i][1]:
            portalizacao = 1
            snake[0] = portalB[random.randint(0, 5)]
            screen.fill((0, 255, 0))


# sistema inversor de direção pros portal(ou não)
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
    global snake, ponto, speed, apple_pos, portal_pos, barrier_pos, my_direction, escolha
    apple_pos = on_grid_random()
    my_direction = LEFT
    portal_pos = [(on_grid_random()), (on_grid_random())]
    barrier_pos = [(on_grid_random()), on_grid_random(), on_grid_random(), on_grid_random(), on_grid_random()]
    snake = [(200, 200), (210, 200), (220, 200)]
    ponto = 0
    speed = 10
    escolha = 0


# função que define uma coordenada aleatória
def on_grid_random():
    x = random.randint(40, 610)
    y = random.randint(70, 640)
    # retorna os valores para que possam ser usados no jogo,
    # e para ficarem precisos em relação ao grid são multiplicados por 10
    return x // 10 * 10, y // 10 * 10

# sistema de detecção de clip aleatorizador (ta ruim pra krl kkkkkk)
def collidcheck(a1, b2):
    if a1 == b2:
        a1 = on_grid_random()


# sistema de colisão
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

pygame.init()
# tamanho da tela(600x600)
screen = pygame.display.set_mode((660, 690))
# nome que irá aparecer na janela
pygame.display.set_caption('NeonSnake')

# fonte definida pro placar
font = pygame.font.Font("PressStart2P.ttf", 11)
font2 = pygame.font.Font("PressStart2P.ttf", 30)
#font2 = pygame.font.SysFont("Arial", 30)

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

# portais fixos
# portal de cima
portalC_pos = [(300, 50), (310, 50), (320, 50), (330, 50), (340, 50), (350, 50)]
# portal de baixo
portalB_pos = [(300, 660), (310, 660), (320, 660), (330, 660), (340, 660), (350, 660)]
# portal da esquerda
portalE_pos = [(20, 340), (20, 350), (20, 360), (20, 370), (20, 380), (20, 390)]
# portal da direita
portalD_pos = [(630, 340), (630, 350), (630, 360), (630, 370), (630, 380), (630, 390)]
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
# cor padrão da fonte do placar
cor = cor2 = (255, 255, 0)
clock = pygame.time.Clock()
escolha = portalizacao = ponto = 0

hs = 0



jogo_ativo = 1
while jogo_ativo == 1:
    # Taxa de atualização do jogo, o padrão é 20 clocks por segundo
    clock.tick(speed)
    portalizacao = 0

    d = shelve.open('score.txt')
    hs = d['score']

    ######## placar de status ##########
    # tamanho
    size_font = font.render("TAMANHO:{tamanho} blocos".format(tamanho=len(snake)), True, cor)
    size_rect = size_font.get_rect()
    size_rect.topleft = (20, 14)
    # pontuação
    score_font = font.render("| {ponto} PTs |".format(ponto=ponto), True, cor2)
    score_rect = score_font.get_rect()
    score_rect.midtop = (660 / 2 + 80, 14)
    # maior pontuação (WIP)
    hs_font = font.render("MAIOR PT:{highscore}".format(highscore=hs), True, cor)
    hs_rect = hs_font.get_rect()
    hs_rect.midtop = (660 / 2 - 40, 14)
    # velocidade
    vel_font = font.render("VELOCIDADE: {clock}X".format(clock=speed - 9), True, cor)
    vel_rect = vel_font.get_rect()
    vel_rect.topleft = (480, 14)

    # cor do fundo da janela(padrão 0,0,0 preto)
    screen.fill((0, 0, 0))
    # cor da tela principal
    gamescreen_skin.fill((0, 0, 0))

    # controles do jogo
    for event in pygame.event.get():
        # input para que ao apertar o "X" o jogo feche
        if event.type == QUIT:
            print("Você fechou o jogo!")
            pygame.quit()
            sys.exit()

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
                pause()

    ###### ações após colisão entre a maçã e a cobra ########
    if collision(snake[0], apple_pos):
        # gerado novo spawn pra maçã
        apple_pos = on_grid_random()
        # piscada maneira
        screen.fill(randomcolor())
        # aumentado o lenght da cobra
        snake.append((0, 0))
        # os elementos são aleatorizados
        jooj_pos = (on_grid_random())
        portal_pos = [(on_grid_random()), (on_grid_random())]
        barrier_pos = [(on_grid_random()), on_grid_random(), on_grid_random(), on_grid_random(), on_grid_random()]
        # aumentado a pontuação
        ponto = ponto + 1
        # sistema que decide se o jooj vai aparecer ou não
        if ponto > 5:
            escolha = random.randint(0, 3)
            if ponto == 1:
                print("jooj ativado!")
        # aumentado a velocidade
        if speed < 15:
            speed = speed + 1
        elif 15 <= speed < 20:
            speed = speed + 0.5
        elif speed >= 20:
            speed = speed + 0.25
        #save temporario de pontuação
        if ponto > hs:
            hs = ponto
            d['score'] = hs
            d.close()

    # impede que a maçã e as barreiras fiquem na mesma coord
    collidcheck(apple_pos, barrier_pos)
    # impede que o portais e as barreiras fiquem na mesma coord
    collidcheck(portal_pos[0], barrier_pos)
    collidcheck(portal_pos[1], barrier_pos)
    # impede que os portais e a maçã fiquem na mesma coord
    collidcheck(portal_pos[0], apple_pos)
    collidcheck(portal_pos[1], apple_pos)

    # efeito colorido na cobra
    snake_skin.fill(randomcolor())

    # efeito no placar caso atingido uma pontuação especifica
    if ponto > hs:
        cor2 = randomcolor()
    else:
        cor2 = 255, 255, 0

    # sistema de colisão entre a cobra e as barreiras(versão lenght enhanced :D)
    for i in range(0, len(barrier_pos)):
        if snake[0][0] == barrier_pos[i][0] and snake[0][1] == barrier_pos[i][1]:
            speed = 1
            gamescreen_skin.fill((255, 0, 0))
            print("Morte: bateu em uma barreira")
            resetador()

    # sistema de colisão dos portais fixos (sim ficou esse código gigante mas consegui diminuir um pouco)
    # portal cima
    if collision(snake[0], portalC_pos[0]) or collision(snake[0], portalC_pos[1]) or collision(snake[0], portalC_pos[2]) or collision(snake[0], portalC_pos[3]) or collision(snake[0], portalC_pos[4]) or collision(snake[0], portalC_pos[5]):
        portfixo(portalC_pos, portalB_pos)
    # portal baixo
    elif collision(snake[0], portalB_pos[0]) or collision(snake[0], portalB_pos[1]) or collision(snake[0], portalB_pos[2]) or collision(snake[0], portalB_pos[3]) or collision(snake[0], portalB_pos[4]) or collision(snake[0], portalB_pos[5]):
        portfixo(portalB_pos, portalC_pos)
    # portal direita
    elif collision(snake[0], portalD_pos[0]) or collision(snake[0], portalD_pos[1]) or collision(snake[0], portalD_pos[2]) or collision(snake[0], portalD_pos[3]) or collision(snake[0], portalD_pos[4]) or collision(snake[0], portalD_pos[5]):
        portfixo(portalD_pos, portalE_pos)
    # portal esquerda
    elif collision(snake[0], portalE_pos[0]) or collision(snake[0], portalE_pos[1]) or collision(snake[0], portalE_pos[2]) or collision(snake[0], portalE_pos[3]) or collision(snake[0], portalE_pos[4]) or collision(snake[0], portalE_pos[5]):
        portfixo(portalE_pos, portalD_pos)

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
        elif speed < 10:
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
        if portalizacao == 0:
            print("Morte: saiu da área permitida")
            gamescreen_skin.fill((255, 0, 0))
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

    # aparentemente, fazem os elementos serem desenhados em todos os clocks(resumi legal agr pra apenas uma função)
    render(tb=0)

    # função que fazerá a tela do jogo atualizar após o final de cada clock(ou while)
    pygame.display.update()
