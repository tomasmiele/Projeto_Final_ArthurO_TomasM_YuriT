import pygame
import os
from config import BOTAO_HEIGHT, BOTAO_WIDTH, HEIGHT, IMG_DIR, SND_DIR, PERSONAGEM_WIDTH, MONSTRO_WIDTH, PERSONAGEM_HEIGHT, MONSTRO_HEIGHT, WIDTH, BLACKOUT_WIDTH, BLACKOUT_HEIGHT, CHAVE_WIDTH, CHAVE_HEIGHT

SWOOSH_SOUND =  'swoosh_sound'
BACKGROUND = 'background'
BOTAO_JOGAR  = 'jogar'
PERSONAGEM_PRINCIPAL = 'personagem_principal'
MONSTRO = 'monstro'
MONSTRO2 = 'monstro2'
MONSTRO3 = 'monstro3'
MONSTRO4 = 'monstro4'
MONSTRO5 = 'monstro5'
CHAO_CASTELO = 'chao_castelo'
PAREDE = 'parede'
PAREDE2 = 'parede2'
PAREDE3 = 'parede3'
PAREDE4 = 'parede4'
PAREDE5 = 'parede5'
ANIMACAO_DIREITA = 'animacao_direita'
ANIMACAO_ESQUERDA = 'animacao_esquerda'
PARADO=  'parado'
PLAYER=  'player'
BLACKOUT = 'blackout'
CHAVE = 'chave'

def load_assets():
    assets = {}

    #imagens
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'castelo.png')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))
    assets[BOTAO_JOGAR] = pygame.image.load(os.path.join(IMG_DIR, 'botao_jogar.png')).convert_alpha()
    assets[BOTAO_JOGAR] = pygame.transform.scale(assets[BOTAO_JOGAR], (BOTAO_WIDTH, BOTAO_HEIGHT))
    assets[MONSTRO] = pygame.image.load(os.path.join(IMG_DIR, 'monstro.png')).convert_alpha()
    assets[MONSTRO] = pygame.transform.scale(assets[MONSTRO], (MONSTRO_WIDTH, MONSTRO_HEIGHT))
    assets[MONSTRO2] = pygame.image.load(os.path.join(IMG_DIR, 'Monstro2.png')).convert_alpha()
    assets[MONSTRO2] = pygame.transform.scale(assets[MONSTRO2], (MONSTRO_WIDTH, MONSTRO_HEIGHT))
    assets[MONSTRO3] = pygame.image.load(os.path.join(IMG_DIR, 'Monstro3.png')).convert_alpha()
    assets[MONSTRO3] = pygame.transform.scale(assets[MONSTRO3], (MONSTRO_WIDTH, MONSTRO_HEIGHT))
    assets[MONSTRO4] = pygame.image.load(os.path.join(IMG_DIR, 'Monstro4.png')).convert_alpha()
    assets[MONSTRO4] = pygame.transform.scale(assets[MONSTRO4], (MONSTRO_WIDTH, MONSTRO_HEIGHT))
    assets[MONSTRO5] = pygame.image.load(os.path.join(IMG_DIR, 'Monstro5.png')).convert_alpha()
    assets[MONSTRO5] = pygame.transform.scale(assets[MONSTRO5], (MONSTRO_WIDTH, MONSTRO_HEIGHT))
    assets[CHAO_CASTELO] = pygame.image.load(os.path.join(IMG_DIR, 'chao_castelo.png')).convert()
    assets[CHAO_CASTELO] = pygame.transform.scale(assets[CHAO_CASTELO], (WIDTH, HEIGHT))
    assets[BLACKOUT] = pygame.image.load(os.path.join(IMG_DIR, 'Blackout.png')).convert_alpha()
    assets[BLACKOUT] = pygame.transform.scale(assets[BLACKOUT], (BLACKOUT_WIDTH, BLACKOUT_HEIGHT))
    assets[CHAVE] = pygame.image.load(os.path.join(IMG_DIR, 'chave.png')).convert_alpha()
    assets[CHAVE] = pygame.transform.scale(assets[CHAVE], (CHAVE_WIDTH, CHAVE_HEIGHT))

    #Estados do personagem

    assets[PARADO] = pygame.image.load(os.path.join(IMG_DIR, 'parado.png')).convert_alpha()
    assets[PARADO] = pygame.transform.scale(assets[PARADO], (PERSONAGEM_WIDTH, PERSONAGEM_HEIGHT))

    #animação de andar
    animacao_direita = []
    for i in range(8):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(IMG_DIR, '{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (PERSONAGEM_WIDTH, PERSONAGEM_HEIGHT))
        animacao_direita.append(img)
    assets[ANIMACAO_DIREITA] = animacao_direita
    
    animacao_esquerda = []
    for i in range(8):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(IMG_DIR, 'esquerda{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (PERSONAGEM_WIDTH, PERSONAGEM_HEIGHT))
        animacao_esquerda.append(img)
    assets[ANIMACAO_ESQUERDA] = animacao_esquerda


    #Paredes
    assets[PAREDE] = pygame.image.load(os.path.join(IMG_DIR, 'Parede.png')).convert()
    assets[PAREDE] = pygame.transform.scale(assets[PAREDE], (40, 40))
    assets[PAREDE2] = pygame.image.load(os.path.join(IMG_DIR, 'Parede2.png')).convert()
    assets[PAREDE2] = pygame.transform.scale(assets[PAREDE2], (40, 40))
    assets[PAREDE3] = pygame.image.load(os.path.join(IMG_DIR, 'Parede3.png')).convert()
    assets[PAREDE3] = pygame.transform.scale(assets[PAREDE3], (40, 40))
    assets[PAREDE4] = pygame.image.load(os.path.join(IMG_DIR, 'Parede4.png')).convert()
    assets[PAREDE4] = pygame.transform.scale(assets[PAREDE4], (40, 40))
    assets[PAREDE5] = pygame.image.load(os.path.join(IMG_DIR, 'Parede5.png')).convert()
    assets[PAREDE5] = pygame.transform.scale(assets[PAREDE5], (40, 40))

    #sons
    pygame.mixer.music.load(os.path.join(SND_DIR, 'musica_principal.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[SWOOSH_SOUND]= pygame.mixer.Sound(os.path.join(SND_DIR, 'swoosh_de_terror.wav'))
    
    return assets