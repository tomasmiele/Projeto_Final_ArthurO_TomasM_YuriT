from curses import window
import time
import random
from matplotlib import image
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
    def __init__(self, x, y, image, paredes):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speedx = 0
        self.speedy = 0
        self.paredes = paredes
        self.currentsprite = 0

    def parar(self,image):
        self.image = image

    def direita(self,anim):
        self.currentsprite+=1
        if self.currentsprite>len(anim)-1:
            self.currentsprite=0
        self.image=anim[self.currentsprite]
    
    def esquerdo(self,anim):
        self.currentsprite+=1
        if self.currentsprite>len(anim)-1:
            self.currentsprite=0
        self.image=anim[self.currentsprite]

    def update(self,personagem2):
        # Atualização da posição do personagem
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
        
        #evita ele passar por cima da parede
        collisions = pygame.sprite.spritecollide(self, self.paredes, False)
        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0:
                self.speedx = 0
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.speedx = 0
            elif self.speedy < 0:
                self.speedy = 0
            elif self.speedy > 0:
                self.speedy = 0

class Monstro(pygame.sprite.Sprite):
    def __init__(self, img, paredes):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        x = random.randint(40, WIDTH - 40)
        y = random.randint(40, HEIGHT - 40)
        if 570 <= x <= 580 or 557 <= y <= 567:
            x = 575
            y = 5
        self.rect.topleft = (x, y)
        self.speedx = random.randint(-1, 1)
        self.speedy = random.randint(-1, 1)
        if self.speedx == 0:
            self.speedx = 1
        if self.speedy == 0:
            self.speedy = 1
        self.paredes = paredes

    def update(self,personagem2):
        # Atualizando a posição do monstro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Evita que o monstro passe pela tela
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

        #evita ele passar por cima da parede
        collisions = pygame.sprite.spritecollide(self, self.paredes, False)
        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
                self.speedx = -self.speedx
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right
                self.speedx = -self.speedx
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                self.speedy = -self.speedy
            elif self.speedy > 0:
                self.rect.bottom = collision.rect.top
                self.speedy = -self.speedy


class Wall(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Blackout(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedx = 0
        self.speedy = 0

    def update(self,personagem2):
        # Atualização da posição do personagem

        self.rect.x = personagem2.rect.x-1188
        self.rect.y = personagem2.rect.y-585

class Chave(pygame.sprite.Sprite):
    def __init__(self, image, lista):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        posicao = lista[random.randint(0, len(lista) - 1)]
        self.x = posicao[0]
        self.y = posicao[1]
        lista.remove(posicao)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
    '''
    def update(self,personagem2):
        collisions = pygame.sprite.spritecollide(self, personagem2, True)
        for collision in collisions:
            if '''
