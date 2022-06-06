import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT, VITORIA, MORTE
from init_screen import init_screen
from game_screen import game_screen
from vitoria_screen import vitoria_screen
from jogar_novamente_screen import jogar_novamente_screen

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Castelo Assombrado')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == VITORIA:
        state = vitoria_screen(window)
    elif state == MORTE:
        state = jogar_novamente_screen(window)
    else:
        state = QUIT
 
pygame.quit() 