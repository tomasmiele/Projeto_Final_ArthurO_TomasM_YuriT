import pygame
import os
from config import IMG_DIR

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load(os.path.join(IMG_DIR, 'https://p4.wallpaperbetter.com/wallpaper/306/264/982/pixel-art-castle-fantasy-art-clouds-dark-hd-wallpaper-preview.jpg')).convert()