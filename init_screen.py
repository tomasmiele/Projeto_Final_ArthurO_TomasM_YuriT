# Importa e inicia pacotes
from matplotlib.pyplot import draw
import pygame
import random
from os import path
from config import BLACK, BOTAO_HEIGHT, BOTAO_WIDTH, FPS, IMG_DIR, WIDTH, HEIGHT, INIT, GAME, QUIT
from assets import BACKGROUND, BOTAO_JOGAR, load_assets
from sprites import Button

def init_screen(window):
    assets = load_assets()

    # Carrega o fundo da tela inicial
    background = assets[BACKGROUND]
    background_rect = background.get_rect()

    img_botao = assets[BOTAO_JOGAR]
    botao = Button(WIDTH/2-224, HEIGHT/2+15, img_botao, 0.5)

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