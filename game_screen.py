from numpy import False_
import pygame
from sympy import Q
from mapa import matriz
from os import path
from config import BLACK, FPS, GAME, QUIT, VITORIA, WHITE, WIDTH, HEIGHT, IMG_DIR, MORTE
from assets import ANIMACAO_DIREITA, ANIMACAO_ESQUERDA, BLACKOUT, CHAO_CASTELO, MONSTRO, MONSTRO2,MONSTRO3,MONSTRO4,MONSTRO5, PARADO, load_assets, CHAVE, PORTA
from sprites import Blackout, Personagem, Monstro, Chave, Pontos, Porta
from scene import make
from posicoes_chave import posicoes
from posicoes_monstro import lista_mov, lista_mov2,lista_mov3,lista_mov4,lista_mov5

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()
    all_sprites = pygame.sprite.Group()
    all_chaves = pygame.sprite.Group()
    all_monstros = pygame.sprite.Group()
    all_personagem_principal = pygame.sprite.Group()
    all_blackout = pygame.sprite.Group()
    all_pontos_chaves = pygame.sprite.Group()
    all_porta = pygame.sprite.Group()
    tempo=0
    tempo2=0
    tempo3=0
    tempo4=0
    tempo5=0

    background = pygame.image.load(path.join(IMG_DIR, 'chao_castelo.png')).convert()
    background_rect = background.get_rect()
    personagem_principal = pygame.image.load(path.join(IMG_DIR, 'parado.png')).convert_alpha()
    monstro = pygame.image.load(path.join(IMG_DIR, 'monstro.png')).convert_alpha()
    monstro2 = pygame.image.load(path.join(IMG_DIR, 'monstro2.png')).convert_alpha()
    monstro3 = pygame.image.load(path.join(IMG_DIR, 'monstro3.png')).convert_alpha()
    monstro4 = pygame.image.load(path.join(IMG_DIR, 'monstro4.png')).convert_alpha()
    monstro5 = pygame.image.load(path.join(IMG_DIR, 'monstro5.png')).convert_alpha()

    all_walls = make(matriz)

    img_personagem_principal = assets[PARADO]
    personagem_principal = Personagem(575, 562, img_personagem_principal, all_walls)
    img_monstro = assets[MONSTRO]
    monstro = Monstro(img_monstro, all_walls,565,40)
    img_monstro2 = assets[MONSTRO2]
    monstro2 = Monstro(img_monstro2, all_walls,1125,40)
    img_monstro3 = assets[MONSTRO3]
    monstro3 = Monstro(img_monstro3, all_walls,1125,400)
    img_monstro4 = assets[MONSTRO4]
    monstro4 = Monstro(img_monstro4, all_walls,445,440)
    img_monstro5 = assets[MONSTRO5]
    monstro5 = Monstro(img_monstro5, all_walls,485,40)

    img_blackout = assets[BLACKOUT]
    blackout = Blackout(575, 562, img_blackout)
    img_chave = assets[CHAVE]

    img_porta = assets[PORTA]
    porta = Porta(560, 0, img_porta)

    all_sprites.add(porta)
    all_porta.add(porta)
    
    reposicao_chave = []
    for i in range (4):
        chave = Chave(img_chave, posicoes)
        reposicao_chave.append([chave.x, chave.y])
        all_sprites.add(chave)
        all_chaves.add(chave)
    
    for i in range (4):
        posicoes.append(reposicao_chave[i])
        
    pontos = 0
    
    all_sprites.add(personagem_principal)
    all_personagem_principal.add(personagem_principal)

    all_sprites.add(monstro)
    all_sprites.add(monstro2)
    all_sprites.add(monstro3)
    all_sprites.add(monstro4)
    all_sprites.add(monstro5)
    all_monstros.add(monstro)
    all_monstros.add(monstro2)
    all_monstros.add(monstro3)
    all_monstros.add(monstro4)
    all_monstros.add(monstro5)

    all_sprites.add(blackout) 
    all_blackout.add(blackout)


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
            state = MORTE
            running = False

        hit = pygame.sprite.spritecollide(personagem_principal, all_chaves, True)
        if hit != []:
            pontos += 1

        hit2 = pygame.sprite.spritecollide(personagem_principal, all_porta, False)
        if hit2 != [] and pontos == 4:
            state = VITORIA   
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
                    personagem_principal.parar(assets[PARADO])
                    personagem_principal.speedy = 0

                if event.key == pygame.K_DOWN:
                    dir_pressionado=False
                    personagem_principal.parar(assets[PARADO])
                    personagem_principal.speedy = 0

        monstro.andar(lista_mov,tempo)
        monstro2.andar(lista_mov2,tempo2)
        monstro3.andar(lista_mov3,tempo3)
        monstro4.andar(lista_mov4,tempo4)
        monstro5.andar(lista_mov5,tempo5)

        tempo+=1
        tempo2+=1
        tempo3+=1
        tempo4+=1
        tempo5+=1
        if tempo>=len (lista_mov):
            tempo=0
        if tempo2>=len (lista_mov2):
            tempo2=0
        if tempo3>=len (lista_mov3):
            tempo3=0
        if tempo4>=len (lista_mov4):
            tempo4=0
        if tempo5>=len (lista_mov5):
            tempo5=0
        
        if esq_pressionado==True:
            personagem_principal.esquerdo(assets[ANIMACAO_ESQUERDA])

        if dir_pressionado==True:
            personagem_principal.direita(assets[ANIMACAO_DIREITA])

        all_sprites.update(personagem_principal) #atualiza a posição do personagem e do monstro

        all_sprites.draw(window)

        all_porta.draw(window)

        all_blackout.draw(window)

        all_personagem_principal.draw(window)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

        x = 10
        for i in range(pontos):
            ponto_chave = Pontos(img_chave, x, 570)
            all_pontos_chaves.add(ponto_chave)
            x += 40
        all_pontos_chaves.draw(window)

        pygame.display.update() # Mostra o novo frame para o jogador
    return state

#window = pygame.display.set_mode((WIDTH, HEIGHT))
#print(game_screen(window))