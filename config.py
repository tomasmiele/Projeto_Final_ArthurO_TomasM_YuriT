from os import path

# Pasta que contêm imagem 
IMG_DIR = path.join(path.dirname(__file__), 'assets','Imagens')
SND_DIR = path.join(path.dirname(__file__), 'assets','Sound')

WIDTH = 1300
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

PERSONAGEM_WIDTH = 50
PERSONAGEM_HEIGHT = 38
MONSTRO_WIDTH = 50
MONSTRO_HEIGHT = 38

INIT = 0
GAME = 1
QUIT = 2