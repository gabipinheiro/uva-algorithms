# Pivoteamento/particionamento: Dado um pivô (valor específico), os elementos de um vetor devem se movimentar até que no final, todos os elementos à direita do pivô serão maiores que ele ou iguais e todos à esquerda serão menores.

# construção da tabela
import random

# tab = []
# for i in range(0,10):
#     tab.append(random.randint(0,100))



# algoritmo: pivoteamento

def pivo(tab):
    pos_p = 0         #posição inicial do pivô (à esquerda)
    p = tab[pos_p]    #pivô
    d=len(tab)-1      #apontador da direita
    e=1               #apontador da esquerda

    while e < d:

        while tab[d]>=p and d>0:
            d=d-1;

        while tab[e]<p and e<(len(tab)-1):
            e=e+1;

        if e<d:
            temp=tab[e];
            tab[e]=tab[d]
            tab[d]=temp;
            e=e+1;
            d=d-1;

    tab[pos_p] = tab[d]
    tab[d] = p

    return (d,tab)

pivo([99,1,2,3,4,10,1,0])