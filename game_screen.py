import pygame
from config import FPS, WIDTH, HEIGHT
from assets import load_assets
#from sprites import 

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    window.fill((0,0,0))  # Preenche com a cor branca
    pygame.display.update()  # Mostra o novo frame para o jogador

window = pygame.display.set_mode((WIDTH, HEIGHT))
print(game_screen(window))