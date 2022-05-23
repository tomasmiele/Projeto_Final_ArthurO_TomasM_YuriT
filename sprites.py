from curses import window
import random
import pygame
from config import WIDTH, HEIGHT
from assets import BOTAO_JOGAR


#classe para fazer com que o botão seja clicavel e mude a tela
class Button():
    def __init__(self,x, y, image, scale, window):
        width = 900
        height = 500
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.cliked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos() #pega a posição do mouse
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.cliked == False:
                self.cliked = True
                action = True
                print('pressionado')
        
        window.blit(self.image, (self.rect.x, self.rect.y))
        #return action
