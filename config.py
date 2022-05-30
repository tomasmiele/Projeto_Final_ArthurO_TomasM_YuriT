from os import path

# Pasta que contêm imagem 
IMG_DIR = path.join(path.dirname(__file__), 'assets','Imagens')
SND_DIR = path.join(path.dirname(__file__), 'assets','Sound')

WIDTH = 1200
HEIGHT = 600
FPS = 30
BLACKOUT_WIDTH = 2400
BLACKOUT_HEIGHT = 1200
BOTAO_WIDTH = 200
BOTAO_HEIGHT = 100
CHAVE_HEIGHT = 30
CHAVE_WIDTH = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

PERSONAGEM_WIDTH = 25
PERSONAGEM_HEIGHT = 30
MONSTRO_WIDTH = 25
MONSTRO_HEIGHT = 30

INIT = 0
GAME = 1
QUIT = 2