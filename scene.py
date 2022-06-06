import pygame
from assets import PAREDE2, load_assets, PAREDE, PAREDE3 ,  PAREDE4 , PAREDE5,PAREDE6
from sprites import Wall
import random

def make(m):
    assets = load_assets()
    all_walls = pygame.sprite.Group()
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 1:
                img_parede = assets[PAREDE]
                x = i * 40
                y = j * 40
                all_walls.add(Wall(img_parede, x, y)) #Wall é pra ser a class das paredes
            elif m[i][j] == 2:
                img_parede = assets[PAREDE2]
                x = i * 40
                y = j * 40
                all_walls.add(Wall(img_parede, x, y)) 
            elif m[i][j] == 3:
                img_parede = assets[PAREDE3]
                x = i * 40
                y = j * 40
                all_walls.add(Wall(img_parede, x, y)) 
            elif m[i][j] == 4:
                img_parede = assets[PAREDE4]
                x = i * 40
                y = j * 40
                all_walls.add(Wall(img_parede, x, y)) 
            elif m[i][j] == 5:
                img_parede = assets[PAREDE5]
                x = i * 40
                y = j * 40
                all_walls.add(Wall(img_parede, x, y)) 
            elif m[i][j] == 6:
                img_parede = assets[PAREDE6]
                x = i * 40
                y = j * 40
                all_walls.add(Wall(img_parede, x, y)) 
    return all_walls