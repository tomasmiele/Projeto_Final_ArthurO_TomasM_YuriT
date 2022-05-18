# Importa e inicia pacotes
import pygame
from config import WIDTH, HEIGHT
pygame.init()

# Tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Título do jogo')

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