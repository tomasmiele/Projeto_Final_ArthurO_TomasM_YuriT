"""lista_mov=[[560,40]]

for i in range(40):
    lista_mov.append([lista_mov[i][0]+1,lista_mov[i][1]+0])

print(lista_mov)"""

lista_mov=[]

def monstro_esquerda(l):
    for i in range(40):
        l.append([-1,0])
    return l


def monstro_baixo(l):
    for i in range(40):
        l.append([0,1])
    return l


def monstro_cima(l):
    for i in range(40):
        l.append([0,-1])
    return l


def monstro_direita(l):
    for i in range(40):
        l.append([1,0])
    return l


for i in range(2):
    monstro_direita(lista_mov)

for i in range(2):
    monstro_baixo(lista_mov)

for i in range(2):
    monstro_esquerda(lista_mov)

for i in range(2):
    monstro_baixo(lista_mov)

for i in range(2):
    monstro_esquerda(lista_mov)

for i in range(2):
    monstro_baixo(lista_mov)

for i in range(2):
    monstro_esquerda(lista_mov)

for i in range(2):
    monstro_baixo(lista_mov)

for i in range(3):
    monstro_esquerda(lista_mov)

for i in range(4):
    monstro_baixo(lista_mov)

for i in range(2):
    monstro_esquerda(lista_mov)

for i in range(3):
    monstro_cima(lista_mov)

for i in range(2):
    monstro_esquerda(lista_mov)

for i in range(3):
    monstro_cima(lista_mov)

for i in range(2):
    monstro_esquerda(lista_mov)

for i in range(6):
    monstro_cima(lista_mov)

for i in range(2):
    monstro_direita(lista_mov)

for i in range(4):
    monstro_baixo(lista_mov)

for i in range(8):
    monstro_direita(lista_mov)

for i in range(2):
    monstro_cima(lista_mov)

for i in range(5):
    monstro_direita(lista_mov)

for i in range(2):
    monstro_cima(lista_mov)

for i in range(2):
    monstro_esquerda(lista_mov)

print(lista_mov)
