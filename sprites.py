from curses import window
import random
import pygame
from config import WIDTH, HEIGHT, PERSONAGEM_WIDTH, MONSTRO_WIDTH, PERSONAGEM_HEIGHT, MONSTRO_HEIGHT
from assets import BOTAO_JOGAR, PERSONAGEM_PRINCIPAL, MONSTRO

#classe para fazer com que o botão seja clicavel e mude a tela
class Button():
    def __init__(self,x, y, image, scale):
        width = 900
        height = 500
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.cliked = False

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def press(self):
        action = False
        pos = pygame.mouse.get_pos() #pega a posição do mouse
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.cliked == False:
                self.cliked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.cliked = False
        return action

class Personagem(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
    
class Monstro(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        self.rect.topleft = (x, y)
        self.speedx = random.randint(-1, 1)
        self.speedy = random.randint(-1, 1)
        if self.speedx == 0:
            self.speedx = 1
        if self.speedy == 0:
            self.speedy = 1

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.speedx = -self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = -self.speedx
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speedy = -self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy = -self.speedy