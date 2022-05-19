# Importa e inicia pacotes
import pygame
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from assets import BACKGROUND, BOTAO_JOGAR, SWOOSH_SOUND, load_assets

pygame.init()
pygame.mixer.init()

# Tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Título do jogo')
assets = load_assets()

fundo = assets[BACKGROUND]
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
    window.blit(fundo, (0,0))
    botao=assets[BOTAO_JOGAR]
    botao=pygame.transform.scale(botao,(900,500))
    window.blit(botao,(WIDTH/5,HEIGHT/5))

    # ---- Atualiza o estado do jogo
    pygame.display.update()

# ==== FINALIZAÇÃO ====
pygame.quit()