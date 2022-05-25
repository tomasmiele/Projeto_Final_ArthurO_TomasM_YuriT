import pygame
from assets import load_assets, PAREDE
from sprites import Wall

def make(m):
    assets = load_assets()
    img_parede = assets[PAREDE]
    all_walls = pygame.sprite.Group()
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 1:
                x = i * 20
                y = j * 20
                all_walls.add(Wall(img_parede, x, y)) #Wall é pra ser a class das paredes
    return all_walls