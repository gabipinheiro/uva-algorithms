# empilha, desempilha, multi Desempilha
import random

class Pilha:

    # Método Construtor
    def __init__(self, size):
        self.size = size;
        self.pilha = [None for i in range(0,size)];
        self.t = -1; #topo

        print("Criada pilha de ",size," elementos: ", self.pilha)


    def empilha(self, element):

        # verifica posição do topo pra saber se tem espaço pra empilhar
        if self.t>= (len(self.pilha))-1:
            print('Empilha elemento',element,' - Pilha cheia ', self.pilha);
        else:
            self.t = self.t+1;
            self.pilha[self.t] = element;
            print('Empilha elemento',element, ' - ', self.pilha);


    def desempilha(self):

        # verifica posição do topo pra saber se tem elemento pra desempilhar
        if self.t<=-1:
            print('Desempilha - Pilha vazia');
        else:
            element = self.pilha[self.t]
            self.pilha[self.t] = None;
            self.t = self.t-1;
            print('Desempilha elemento',element, ' - ', self.pilha)


    def multidesempilha(self, qtt):

        elements = [] # para guardar os elementos desempilhados
        for i in range(self.t,self.t-qtt, -1):
            if i>-1: # verifica se tem elemento para desempilhar
                elements.append(self.pilha[self.t])
                self.pilha[self.t]=None
                self.t=self.t-1

        print('Multidesempilha',qtt,'elementos',elements, ' - ', self.pilha)


#criando pilha de 10 elementos
pilha = Pilha(10)

#empilhando 9 elementos
for i in range(0, 9):
    pilha.empilha(random.randint(0, 10))

#desempilhando 2 elementos
for i in range(0,3):
    pilha.desempilha();

#multidesempilhando 3
pilha.multidesempilha(3);
