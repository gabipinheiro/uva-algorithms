# Maximo: Determinar o valor máximo de um conjunto armazenado em uma tabela tab de n valores

# construção da tabela
import random

lista = []
for i in range(0,10):
    lista.append(random.randint(0,100))

print('tabela: ',lista)


# algoritmo: maximo

def maximo (tab):

    max = tab[0]; # maximo inicia com o valor da primeira posicao da tabela

    for i in range(1,len(tab)):
        current = tab[i];

        if current > max:
            max = current;

    return max

maximo(lista)