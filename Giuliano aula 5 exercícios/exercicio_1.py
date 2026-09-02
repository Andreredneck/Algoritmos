def busca_sequencial_multipla(lista, chave):
    posicoes = []
    for i in range(len(lista)):
        if lista[i] == chave:
            posicoes.append(i)
    return posicoes

# exemplo de uso:

dados = [10, 20, 30, 40,50,60]
print(busca_sequencial_multipla(dados, 20))
print(busca_sequencial_multipla(dados, 70))