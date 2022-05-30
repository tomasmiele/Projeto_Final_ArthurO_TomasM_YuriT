import pygame
from sympy import Q
from mapa import matriz
from os import path
from config import BLACK, FPS, GAME, QUIT, WHITE, WIDTH, HEIGHT, IMG_DIR
from assets import ANIMACAO_DIREITA, ANIMACAO_ESQUERDA, BLACKOUT, CHAO_CASTELO, MONSTRO, PARADO, load_assets
from sprites import Blackout, Personagem, Monstro
from scene import make

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()
    all_sprites = pygame.sprite.Group()
    all_monstros = pygame.sprite.Group()
    all_personagem_principal = pygame.sprite.Group()

    background = pygame.image.load(path.join(IMG_DIR, 'chao_castelo.png')).convert()
    background_rect = background.get_rect()
    personagem_principal = pygame.image.load(path.join(IMG_DIR, 'parado.png')).convert_alpha()
    monstro = pygame.image.load(path.join(IMG_DIR, 'monstro.png')).convert_alpha()

    all_walls = make(matriz)

    img_personagem_principal = assets[PARADO]
    personagem_principal = Personagem(575, 562, img_personagem_principal, all_walls)
    img_monstro = assets[MONSTRO]
    monstro = Monstro(img_monstro, all_walls)
    img_blackout = assets[BLACKOUT]
    blackout = Blackout(575, 562, img_blackout)

    all_sprites.add(personagem_principal)
    all_personagem_principal.add(personagem_principal)

    all_sprites.add(monstro)
    all_monstros.add(monstro)

    all_sprites.add(blackout)

    esq_pressionado=False #usado na animação

    dir_pressionado=False #usado na animação

    relogio=0 #usado na velocidade da animação

    for s in all_walls.sprites():
        all_sprites.add(s)
    
    running = True
    while running:
        clock.tick(FPS)
        window.fill(BLACK)
        window.blit(assets[CHAO_CASTELO], background_rect)

        #se o monstro bater no personagem principal ele morre e acaba o jogo
        hits = pygame.sprite.spritecollide(personagem_principal, all_monstros, False)
        if hits != []:
            state = QUIT
            running = False

        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
                
                if event.key == pygame.K_RIGHT:
                    personagem_principal.speedx += 1
                    dir_pressionado=True #animação de andar para direita

                if event.key == pygame.K_UP :
                    personagem_principal.speedy -= 1
                    dir_pressionado=True #animação de andar para direita

                if event.key == pygame.K_DOWN :
                    personagem_principal.speedy += 1
                    dir_pressionado=True #animação de andar para direita

                if event.key == pygame.K_LEFT :
                    personagem_principal.speedx -= 1
                    esq_pressionado=True
            
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    personagem_principal.speedx = 0
                    esq_pressionado=False
                    personagem_principal.parar(assets[PARADO])

                if event.key == pygame.K_RIGHT:
                    personagem_principal.speedx = 0
                    dir_pressionado=False
                    personagem_principal.parar(assets[PARADO])

                if event.key == pygame.K_UP:
                    dir_pressionado=False
                    personagem_principal.speedy = 0

                if event.key == pygame.K_DOWN:
                    dir_pressionado=False
                    personagem_principal.speedy = 0
        
        if esq_pressionado==True:
            personagem_principal.esquerdo(assets[ANIMACAO_ESQUERDA])

        if dir_pressionado==True:
            personagem_principal.direita(assets[ANIMACAO_DIREITA])

        all_sprites.update(personagem_principal) #atualiza a posição do personagem e do monstro

        all_sprites.draw(window)

        all_personagem_principal.draw(window)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

        pygame.display.update() # Mostra o novo frame para o jogador
    return state

#window = pygame.display.set_mode((WIDTH, HEIGHT))
#print(game_screen(window))