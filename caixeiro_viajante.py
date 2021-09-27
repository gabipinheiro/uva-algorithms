#caixeiro viajante - teoria do vizinho mais proximo

# Selecionar aleatoriamente uma cidade inicial (ponto de partida)
# Para escolha da próxima cidade, examinar todas as cidades que ainda não foram visitadas e selecionar a que estiver mais perto da atual.
# Vá para esta cidade e repita esta etapa até todas as cidades terem sido visitadas.
# No final, volte para a primeira cidade.

cidades = ['Rio de Janeiro','Duque de Caxias','São João de Meriti','Seropédica'];
distancias = [[0,25,31,75],
            [25,0,7,52],
            [31,7,0,48],
            [75,52,48,0],
            ]

def cidade_de_origem(cidade):
    # valores iniciais
    cidade_origem=cidade;
    visitadas = [cidade_origem]
    cidade_atual=cidade_origem;

    encontra_rota(cidade_origem,visitadas,cidade_atual)


# função que verifica se uma cidade já foi visitada
def verifica_visita(cidade,visitadas):
    for j in visitadas:
        if cidade == j:
            return True;
    return False

def encontra_rota(cidade_origem,visitadas,cidade_atual):
    # itera até que todas as cidades tenham sido visitadas
    while len(visitadas) < len(cidades):

        # usado para encontrar a cidade de menor distancia)
        menor_distancia=0

        # a partir da cidade atual, verifica qual a mais próxima que ainda não foi visitada
        for i in distancias[cidade_atual]:
            posicao_cidade_atual = distancias[cidade_atual].index(i)

            if i==0:
                continue

            if verifica_visita(posicao_cidade_atual,visitadas):
                continue

            if i<menor_distancia or menor_distancia==0:
                menor_distancia=i

        cidade_atual = distancias[cidade_atual].index(menor_distancia)
        visitadas.append(cidade_atual)

    # ultima posição deve ser a cidade de origem
    visitadas.append(cidade_origem)

    melhor_rota = []
    for i in visitadas:
        melhor_rota.append(cidades[i])

    print('Partindo de',cidades[i],':',melhor_rota)

print("Cidades: ",cidades)

#testando todas as entradas
cidade_de_origem(cidades.index('Rio de Janeiro'));
cidade_de_origem(cidades.index('Duque de Caxias'));
cidade_de_origem(cidades.index('São João de Meriti'));
cidade_de_origem(cidades.index('Seropédica'));



