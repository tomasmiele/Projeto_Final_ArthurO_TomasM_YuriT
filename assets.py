import pygame
import os
from config import HEIGHT, IMG_DIR, SND_DIR, PERSONAGEM_WIDTH, MONSTRO_WIDTH, PERSONAGEM_HEIGHT, MONSTRO_HEIGHT, WIDTH

SWOOSH_SOUND =  'swoosh_sound'
BACKGROUND = 'background'
BOTAO_JOGAR  = 'jogar'
PERSONAGEM_PRINCIPAL = 'personagem_principal'
MONSTRO = 'monstro'
CHAO_CASTELO = 'chao_castelo'
PAREDE = 'parede'

def load_assets():
    assets = {}
    #imagens
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'castelo.png')).convert()
    assets[BOTAO_JOGAR] = pygame.image.load(os.path.join(IMG_DIR, 'botao_jogar.png')).convert_alpha()
    assets[PERSONAGEM_PRINCIPAL] = pygame.image.load(os.path.join(IMG_DIR, 'personagem_principal.png')).convert_alpha()
    assets[PERSONAGEM_PRINCIPAL] = pygame.transform.scale(assets[PERSONAGEM_PRINCIPAL], (PERSONAGEM_WIDTH, PERSONAGEM_HEIGHT))
    assets[MONSTRO] = pygame.image.load(os.path.join(IMG_DIR, 'monstro.png')).convert_alpha()
    assets[MONSTRO] = pygame.transform.scale(assets[MONSTRO], (MONSTRO_WIDTH, MONSTRO_HEIGHT))
    assets[CHAO_CASTELO] = pygame.image.load(os.path.join(IMG_DIR, 'chao_castelo.png')).convert()
    assets[CHAO_CASTELO] = pygame.transform.scale(assets[CHAO_CASTELO], (WIDTH, HEIGHT))
    assets[PAREDE] = pygame.image.load(os.path.join(IMG_DIR, 'parede.png')).convert()
    assets[PAREDE] = pygame.transform.scale(assets[PAREDE], (20, 20))

    #sons
    pygame.mixer.music.load(os.path.join(SND_DIR, 'musica_principal.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[SWOOSH_SOUND]= pygame.mixer.Sound(os.path.join(SND_DIR, 'swoosh_de_terror.wav'))
    
    return assets