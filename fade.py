import pygame
from config import WIDTH, HEIGHT

def fade(WIDTH, HEIGHT):
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill((0,0,0))
    return fade