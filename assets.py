import pygame
import os
from config import IMG_DIR

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load(os.path.join(IMG_DIR, 'castelo.png')).convert()
    
    return assets