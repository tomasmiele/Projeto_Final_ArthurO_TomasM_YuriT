import pygame
from os import path
from config import BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, IMG_DIR
from assets import load_assets
#from sprites import 

def game_screen(window):
    state = GAME
    # Variável para o ajuste de velocidade
    #clock = pygame.time.Clock()

    background = pygame.image.load(path.join(IMG_DIR, 'chao_castelo.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:
        # A cada loop, redesenha o fundo e os sprites
        window.fill(BLACK)
        window.blit(background, background_rect)

        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

        pygame.display.update() # Mostra o novo frame para o jogador
    return state

#window = pygame.display.set_mode((WIDTH, HEIGHT))
#print(game_screen(window))