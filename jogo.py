# Importa e inicia pacotes
import pygame
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen

pygame.init()
pygame.mixer.init()

# Tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Título do jogo')

state = GAME
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    else:
        state = QUIT

# ==== Loop principal ====
game = True
while game:
    # ---- Trata eventos
    for event in pygame.event.get():
        # ---- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ---- Gera saídas
    window.fill((255, 0, 0))

    # ---- Atualiza o estado do jogo
    pygame.display.update()

# ==== FINALIZAÇÃO ====
pygame.quit()