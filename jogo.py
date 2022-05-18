# Importa e inicia pacotes
import pygame
from config import WIDTH, HEIGHT, INIT, GAME, QUIT

pygame.init()
pygame.mixer.init()

# Tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Título do jogo')
image = pygame.image.load('assets/img/https://p4.wallpaperbetter.com/wallpaper/306/264/982/pixel-art-castle-fantasy-art-clouds-dark-hd-wallpaper-preview.jpg').convert()
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
    window.blit(image, (10,10))

    # ---- Atualiza o estado do jogo
    pygame.display.update()

# ==== FINALIZAÇÃO ====
pygame.quit()