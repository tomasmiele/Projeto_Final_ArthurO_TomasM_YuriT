import pygame
from assets import PAREDE2, load_assets, PAREDE, PAREDE3 ,  PAREDE4 , PAREDE5,PAREDE6
from sprites import Wall
import random

def make(m):
    assets = load_assets()
    all_walls = pygame.sprite.Group()
    for i in range(len(m)):
        for j in range(len(m[i])):
            pos_x = i * 40
            pos_y = j * 40
            if m[i][j] == 1:
                img_parede = assets[PAREDE]
                x = pos_x
                y = pos_y
                all_walls.add(Wall(img_parede, x, y)) #Wall é pra ser a class das paredes
            elif m[i][j] == 2:
                img_parede = assets[PAREDE2]
                x = pos_x
                y = pos_y
                all_walls.add(Wall(img_parede, x, y)) 
            elif m[i][j] == 3:
                img_parede = assets[PAREDE3]
                x = pos_x
                y = pos_y
                all_walls.add(Wall(img_parede, x, y)) 
            elif m[i][j] == 4:
                img_parede = assets[PAREDE4]
                x = pos_x
                y = pos_y
                all_walls.add(Wall(img_parede, x, y)) 
            elif m[i][j] == 5:
                img_parede = assets[PAREDE5]
                x = pos_x
                y = pos_y
                all_walls.add(Wall(img_parede, x, y)) 
            elif m[i][j] == 6:
                img_parede = assets[PAREDE6]
                x = pos_x
                y = pos_y
                all_walls.add(Wall(img_parede, x, y)) 
    return all_walls