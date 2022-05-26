import pygame
from sympy import Q
from mapa import matriz
from os import path
from config import BLACK, FPS, GAME, QUIT, WHITE, WIDTH, HEIGHT, IMG_DIR
from assets import CHAO_CASTELO, MONSTRO, PERSONAGEM_PRINCIPAL, load_assets
from sprites import Personagem, Monstro
from scene import make
from fade import fade, circle_surface

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()
    all_sprites = pygame.sprite.Group()
    all_monstros = pygame.sprite.Group()
    all_personagem_principal = pygame.sprite.Group()

    background = pygame.image.load(path.join(IMG_DIR, 'chao_castelo.png')).convert()
    background_rect = background.get_rect()
    personagem_principal = pygame.image.load(path.join(IMG_DIR, 'personagem_principal.png')).convert_alpha()
    monstro = pygame.image.load(path.join(IMG_DIR, 'monstro.png')).convert_alpha()

    all_walls = make(matriz)

    img_personagem_principal = assets[PERSONAGEM_PRINCIPAL]
    personagem_principal = Personagem(575, 562, img_personagem_principal, all_walls)
    posx = 575
    posy = 562
    img_monstro = assets[MONSTRO]
    monstro = Monstro(img_monstro, all_walls)

    all_sprites.add(personagem_principal)
    all_personagem_principal.add(personagem_principal)
    all_sprites.add(monstro)
    all_monstros.add(monstro)

    for s in all_walls.sprites():
        all_sprites.add(s)
    
    running = True
    while running:
        clock.tick(FPS)
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
                if event.key == pygame.K_LEFT and personagem_principal.speedx != 0:
                    personagem_principal.speedx += 1
                if event.key == pygame.K_RIGHT and personagem_principal.speedx != 0:
                    personagem_principal.speedx -= 1
                if event.key == pygame.K_UP and personagem_principal.speedy != 0:
                    personagem_principal.speedy += 1
                if event.key == pygame.K_DOWN and personagem_principal.speedy != 0:
                    personagem_principal.speedy -= 1
        
        all_sprites.update() #atualiza a posição do personagem e do monstro

        all_sprites.draw(window)

        #window.blit(fade(WIDTH, HEIGHT), (0, 0))
        #lanterna = circle_surface(30, (20, 20, 20))
        #window.blit(lanterna, (personagem_principal.posx, personagem_principal.posy), special_flags = pygame.BLEND_ADD)

        #all_personagem_principal.draw(window)

        #se o monstro bater no personagem principal ele morre e acaba o jogo
        hits = pygame.sprite.spritecollide(personagem_principal, all_monstros, False)
        if hits != []:
            state = QUIT
            running = False

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

        pygame.display.update() # Mostra o novo frame para o jogador
    return state

#window = pygame.display.set_mode((WIDTH, HEIGHT))
#print(game_screen(window))