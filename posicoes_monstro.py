"""lista_mov=[[560,40]]

for i in range(40):
    lista_mov.append([lista_mov[i][0]+1,lista_mov[i][1]+0])

print(lista_mov)"""

lista_mov=[]
lista_mov2=[]
lista_mov3=[]
lista_mov4=[]
lista_mov5=[]

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

###monstro 2###

for i in range(8):
    monstro_esquerda(lista_mov2)

for i in range(4):
    monstro_baixo(lista_mov2)

for i in range(2):
    monstro_direita(lista_mov2)

for i in range(2):
    monstro_baixo(lista_mov2)

for i in range(2):
    monstro_direita(lista_mov2)

for i in range(2):
    monstro_cima(lista_mov2)

for i in range(2):
    monstro_direita(lista_mov2)

for i in range(3):
    monstro_baixo(lista_mov2)

for i in range(2):
    monstro_direita(lista_mov2)

for i in range(5):
    monstro_cima(lista_mov2)


for i in range(5):
    monstro_baixo(lista_mov2)

for i in range(2):
    monstro_esquerda(lista_mov2)

for i in range(3):
    monstro_cima(lista_mov2)

for i in range(2):
    monstro_esquerda(lista_mov2)

for i in range(2):
    monstro_baixo(lista_mov2)

for i in range(2):
    monstro_esquerda(lista_mov2)

for i in range(2):
    monstro_cima(lista_mov2)

for i in range(2):
    monstro_esquerda(lista_mov2)

for i in range(4):
    monstro_cima(lista_mov2)

for i in range(8):
    monstro_direita(lista_mov2)



###monstro 3###

for i in range(3):
    monstro_baixo(lista_mov3)

for i in range(27):
    monstro_esquerda(lista_mov3)

for i in range(6):
    monstro_cima(lista_mov3)

for i in range(7):
    monstro_direita(lista_mov3)

for i in range(7):
    monstro_esquerda(lista_mov3)

for i in range(6):
    monstro_baixo(lista_mov3)

for i in range(27):
    monstro_direita(lista_mov3)

for i in range(3):
    monstro_cima(lista_mov3)


###monstro 4###

for i in range(4):
    monstro_esquerda(lista_mov4)

for i in range(2):
    monstro_cima(lista_mov4)

for i in range(3):
    monstro_direita(lista_mov4)

for i in range(2):
    monstro_cima(lista_mov4)

for i in range(5):
    monstro_direita(lista_mov4)

for i in range(4):
    monstro_baixo(lista_mov4)

for i in range(7):
    monstro_direita(lista_mov4)

for i in range(2):
    monstro_baixo(lista_mov4)

for i in range(15):
    monstro_esquerda(lista_mov4)

for i in range(2):
    monstro_cima(lista_mov4)

for i in range(4):
    monstro_direita(lista_mov4)

###monstro 5###

for i in range(5):
    monstro_esquerda(lista_mov5)

for i in range(4):
    monstro_baixo(lista_mov5)

for i in range(4):
    monstro_esquerda(lista_mov5)

for i in range(4):
    monstro_cima(lista_mov5)

for i in range(2):
    monstro_esquerda(lista_mov5)

for i in range(2):
    monstro_direita(lista_mov5)

for i in range(4):
    monstro_baixo(lista_mov5)

for i in range(4):
    monstro_direita(lista_mov5)

for i in range(4):
    monstro_cima(lista_mov5)

for i in range(5):
    monstro_direita(lista_mov5)


