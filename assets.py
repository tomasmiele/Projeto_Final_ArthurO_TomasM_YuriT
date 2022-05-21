import pygame
import os
from config import IMG_DIR, SND_DIR

SWOOSH_SOUND='swoosh_sound'
BACKGROUND='background'
BOTAO_JOGAR='jogar'


def load_assets():
    assets = {}
    #imagens
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'castelo.png')).convert()
    assets[BOTAO_JOGAR] = pygame.image.load(os.path.join(IMG_DIR, 'botao_jogar.png')).convert_alpha()

    #sons
    pygame.mixer.music.load(os.path.join(SND_DIR, 'musica_principal.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[SWOOSH_SOUND]= pygame.mixer.Sound(os.path.join(SND_DIR, 'swoosh_de_terror.wav'))
    
    return assets