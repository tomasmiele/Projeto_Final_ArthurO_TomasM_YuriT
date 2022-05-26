from urllib.parse import SplitResultBytes
import pygame
from config import WIDTH, HEIGHT

def fade(WIDTH, HEIGHT):
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill((0, 0, 0))
    return fade

def circle_surface(raio, cor):
    surface = pygame.Surface((raio * 2, raio * 2))
    pygame.draw.circle(surface, cor, (raio, raio), raio)
    surface.set_colorkey((0, 0, 0))
    return surface