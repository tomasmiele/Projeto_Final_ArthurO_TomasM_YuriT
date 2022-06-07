import pygame
from assets import BOTAO_JOGARN, VITORIA_BG, load_assets
from sprites import Personagem, Button
from sympy import Q
from mapa import matriz2
from os import path
from config import HEIGHT,WIDTH,IMG_DIR, FPS, BLACK, QUIT, GAME
from assets import PARADO, VITORIA_BG, ANIMACAO_DIREITA, ANIMACAO_ESQUERDA, BOTAO_JOGARN2
from scene import make

def jogar_novamente_screen(window):
    clock = pygame.time.Clock()

    assets = load_assets()

    background = pygame.image.load(path.join(IMG_DIR, 'Vitoria.png')).convert()
    background_rect = background.get_rect()

    img_botao = assets[BOTAO_JOGARN2]
    botao = Button(WIDTH/2-225, HEIGHT/2+0, img_botao, 0.5)
    

    running = True
    while running:
        clock.tick(FPS)
        window.fill(BLACK)
        window.blit(assets[VITORIA_BG], background_rect)
        botao.draw(window)

        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if botao.press() == True:
                state = GAME
                running = False

        pygame.display.flip()

    return state