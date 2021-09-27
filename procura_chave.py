# Busca sequencial em tabela: Procurar um valor (chave) em uma tabela (tab) para determinar se chave (ch) encontra-se ou não em tab.

# construção da tabela
import random

tab = []
for i in range(0,10):
    tab.append(random.randint(0,100))

print('tabela: ',tab)


# algoritmo: procura-chave

def find_key (key,tab):

    for i in range(0,len(tab)):
        if key == tab[i]:
            return (True, i)

    return (False)

find_key(random.randint(0,100),tab)


