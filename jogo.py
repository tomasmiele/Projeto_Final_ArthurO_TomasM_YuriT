# Importa e inicia pacotes
import pygame
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from assets import BACKGROUND, BOTAO_JOGAR, SWOOSH_SOUND, load_assets

pygame.init()
pygame.mixer.init()

# Tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Título do jogo')
assets = load_assets()

fundo = assets[BACKGROUND]

#classe para fazer com que o botão seja clicavel e mude a tela
class Button():
    def __init__(self,x, y, image, scale):
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
        #return action
        

        window.blit(self.image, (self.rect.x, self.rect.y))

# ==== Loop principal ====
game = True
while game:
    # ---- Trata eventos
    for event in pygame.event.get():
        # ---- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ---- Gera saídas
    window.fill((255, 0, 0))
    window.blit(fundo, (0,0))
    img_botao = assets[BOTAO_JOGAR]
    botao = Button(488, 258, img_botao, 0.5)
    botao.draw() #deixar assim para aparecer o botao enquanto nao resolver o codigo abaixo
    #if botao.draw() == True:
        #mudar de tela

    # ---- Atualiza o estado do jogo
    pygame.display.update()

# ==== FINALIZAÇÃO ====
pygame.quit()