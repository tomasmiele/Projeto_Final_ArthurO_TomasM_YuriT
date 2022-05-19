from os import path

# Pasta que contêm imagem 
IMG_DIR = path.join(path.dirname(__file__), 'assets','Imagens')
SND_DIR = path.join(path.dirname(__file__), 'assets','Sound')

WIDTH = 1440
HEIGHT = 790

FPS = 30

INIT = 0
GAME = 1
QUIT = 2