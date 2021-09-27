# Busca em profundidade

# x representa jarra 4L
# y representa jarra 3L
# objetivo: (2,n)
# alvo: valor que jarra 4L (x) deve atingir

def busca_profundidade(x,y,alvo):
    print(x, y)

    while True:

        if x == alvo:
            break

        if y == 0:
            y = 3;
            print(x, y)
            continue

        if y != 0 and x == 0:
            x = y
            y = 0
            print(x, y)
            continue

        if x != 0 and x != 4 and y != 0:

            while x < 4:
                x = x + 1
                y = y - 1
                print(x, y)
            continue

        if x == 4:
            x = 0
            print(x, y)
            continue

busca_profundidade(0,0,2)











