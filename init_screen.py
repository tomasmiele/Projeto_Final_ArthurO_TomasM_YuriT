import pygame
import random
from os import path
from config import FPS, GAME, QUIT

def init_screen(screen):
    clock = pygame.time.Clock()
    #background = pygame.image.load(path.join(IMG, 'imagem.png')).convert()
    background = (255, 255, 255)
    background_rect = background.get_rect()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False
        
        screen.fill((255, 255, 255))
        screen.blit(background, background_rect)

        pygame.display.flip()
        
    return state
