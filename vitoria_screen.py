import pygame
from assets import load_assets
from sprites import Personagem
from sympy import Q
from mapa import matriz2
from os import path
from config import HEIGHT,WIDTH,IMG_DIR
from assets import PARADO
from scene import make

def vitoria_screen(window):
    clock = pygame.time.Clock()

    assets = load_assets()
    
    all_walls = make(matriz2)

    all_sprites = pygame.sprite.Group()

    background = pygame.image.load(path.join(IMG_DIR, 'chao_castelo.png')).convert()
    background_rect = background.get_rect()
    personagem_principal = pygame.image.load(path.join(IMG_DIR, 'parado.png')).convert_alpha()

    img_personagem_principal = assets[PARADO]
    personagem_principal = Personagem(575, 562, img_personagem_principal, all_walls)
    all_sprites.add(personagem_principal)

