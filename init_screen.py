# Importa e inicia pacotes
from matplotlib.pyplot import draw
import pygame
import random
from os import path
from config import BLACK, FPS, IMG_DIR, WIDTH, HEIGHT, INIT, GAME, QUIT
from assets import BOTAO_JOGAR, load_assets
from sprites import Button

def init_screen(window):

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'castelo.png')).convert()
    background_rect = background.get_rect()

    assets = load_assets()
    img_botao = assets[BOTAO_JOGAR]
    botao = Button(488, 258, img_botao, 0.5)

    running = True
    while running:

         # A cada loop, redesenha o fundo e os sprites
        window.fill(BLACK)
        window.blit(background, background_rect)
        botao.draw(window)
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if botao.press() == True:
                state = GAME
                running = False

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

        pygame.display.update()
    return state