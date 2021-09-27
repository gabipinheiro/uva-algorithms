#Contador binario - Analise amortizada
#Método contagem

bits = [0,0,0,0];

def incrementa(A,itera):

    #custo amortizado inicia com a soma dos bits 1
    custo_amortizado = 0
    qtdd_operacoes = 0
    for i in A:
        if i==1:
            custo_amortizado = custo_amortizado + 1
    print('Custo amortizado inicial: ',custo_amortizado)

    custo_real = 0 #custo real inicia em 0 (usado para comparar com o custo amortizado)
    for n in range(0,itera):

        #contadores para verificar alterações a cada estado
        altera_de_0_para_1 = 0
        altera_de_1_para_0 = 0
        custo_amortizado_por_estado = 0

        i=len(A)-1
        while i>=0 and A[i] == 1:
            qtdd_operacoes = qtdd_operacoes +1 #contador de operações (n)
            altera_de_1_para_0 = altera_de_1_para_0 + 1

            A[i]=0;
            i=i-1
        if i >= 0:
            qtdd_operacoes = qtdd_operacoes + 1 #contador de operações (n)
            altera_de_0_para_1 = altera_de_0_para_1 + 1

            custo_amortizado=custo_amortizado+2
            custo_amortizado_por_estado = custo_amortizado_por_estado+2
            A[i] = 1
        custo_real = custo_real + altera_de_0_para_1 + altera_de_1_para_0
        print(A, 'Qtdd de alterações: de 0 pra 1 =',altera_de_0_para_1,'e de 1 pra 0 =',altera_de_1_para_0,' - Custo amortizado para este estado: ',custo_amortizado_por_estado,' - Total até o momento é:',custo_amortizado)

    print('Custo real = ', custo_real)
    print('Qtdd operacoes (n) = ',qtdd_operacoes)
    print('Custo amortizado = ', custo_amortizado,'∈ O(n)')


print('bits origem: ',bits)
incrementa(bits,16)
