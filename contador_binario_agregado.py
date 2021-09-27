#Contador binario - Analise amortizada
#Método agregado

bits = [0,0,0,0];

def incrementa(A,itera):

    #contador
    total_incremento=0

    for n in range(0,itera):
        qtdd_inc = 0
        i=len(A)-1
        while i>=0 and A[i] == 1:
            total_incremento=total_incremento+1 #contador
            qtdd_inc = qtdd_inc+1 #contador
            A[i]=0;
            i=i-1
        if i >= 0:
            total_incremento = total_incremento + 1 #contador
            qtdd_inc = qtdd_inc + 1 #contador
            A[i] = 1
        print(A, 'Qtdd de incrementos nesta iteração: ',qtdd_inc)


    print('Total de incrementos nas',itera,'iterações: ',total_incremento)
    print('iterações=',itera,', custo total T(n)=',total_incremento,'. O custo amortizado é T(n)/n = ',total_incremento/itera,' ∈ O(1)')

print('bits origem: ',bits)
incrementa(bits,16)
