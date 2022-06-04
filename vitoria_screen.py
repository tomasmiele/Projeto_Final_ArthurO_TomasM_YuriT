import pygame
from assets import VITORIA_BG, load_assets
from sprites import Personagem
from sympy import Q
from mapa import matriz2
from os import path
from config import HEIGHT,WIDTH,IMG_DIR, FPS, BLACK, QUIT
from assets import PARADO, VITORIA_BG, ANIMACAO_DIREITA, ANIMACAO_ESQUERDA
from scene import make

def vitoria_screen(window):
    clock = pygame.time.Clock()

    assets = load_assets()
    
    all_walls = make(matriz2)

    all_sprites = pygame.sprite.Group()

    background = pygame.image.load(path.join(IMG_DIR, 'Vitoria.png')).convert()
    background_rect = background.get_rect()
    personagem_principal = pygame.image.load(path.join(IMG_DIR, 'parado.png')).convert_alpha()

    img_personagem_principal = assets[PARADO]
    personagem_principal = Personagem(575, 562, img_personagem_principal, all_walls)
    all_sprites.add(personagem_principal)

    esq_pressionado=False #usado na animação

    dir_pressionado=False #usado na animação

    relogio=0 #usado na velocidade da animação

    running = True
    while running:
        clock.tick(FPS)
        window.fill(BLACK)
        window.blit(assets[VITORIA_BG], background_rect)

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
                    personagem_principal.parar(assets[PARADO])
                    personagem_principal.speedy = 0

                if event.key == pygame.K_DOWN:
                    dir_pressionado=False
                    personagem_principal.parar(assets[PARADO])
                    personagem_principal.speedy = 0
        
        if esq_pressionado==True:
            personagem_principal.esquerdo(assets[ANIMACAO_ESQUERDA])

        if dir_pressionado==True:
            personagem_principal.direita(assets[ANIMACAO_DIREITA])

        all_sprites.update(personagem_principal) #atualiza a posição do personagem e do monstro

        all_sprites.draw(window)

        pygame.display.flip()

    return state