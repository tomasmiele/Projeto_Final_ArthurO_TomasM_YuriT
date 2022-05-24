import pygame
from os import path
from config import BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, IMG_DIR
from assets import CHAO_CASTELO, MONSTRO, PERSONAGEM_PRINCIPAL, load_assets
from sprites import Personagem

def game_screen(window):
    # Variável para o ajuste de velocidade
    #clock = pygame.time.Clock()

    assets=load_assets()
    all_sprites = pygame.sprite.Group()

    background = pygame.image.load(path.join(IMG_DIR, 'chao_castelo.png')).convert()
    background_rect = background.get_rect()
    personagem_principal = pygame.image.load(path.join(IMG_DIR, 'personagem_principal.png')).convert_alpha()
    monstro = pygame.image.load(path.join(IMG_DIR, 'monstro.png')).convert_alpha()

    img_personagem_principal = assets[PERSONAGEM_PRINCIPAL]
    personagem_principal = Personagem(100, 0, img_personagem_principal)
    #window.blit(assets[MONSTRO], (#coordenadas de alguma sala sempre aleatório))

    all_sprites.add(personagem_principal)
    
    running = True
    while running:
        window.fill(BLACK)
        window.blit(assets[CHAO_CASTELO], background_rect)

        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                 personagem_principal.speedx -= 1
                if event.key == pygame.K_RIGHT:
                    personagem_principal.speedx += 1
                if event.key == pygame.K_UP:
                    personagem_principal.speedy -= 1
                if event.key == pygame.K_DOWN:
                    personagem_principal.speedy += 1
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    personagem_principal.speedx += 1
                if event.key == pygame.K_RIGHT:
                    personagem_principal.speedx -= 1
                if event.key == pygame.K_UP:
                    personagem_principal.speedy += 1
                if event.key == pygame.K_DOWN:
                    personagem_principal.speedy -= 1
        
        all_sprites.update() #atualiza a posição do personagem e do monstro

        all_sprites.draw(window)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

        pygame.display.update() # Mostra o novo frame para o jogador
    return state

#window = pygame.display.set_mode((WIDTH, HEIGHT))
#print(game_screen(window))