def busca_binaria_ponto_insercao(lista, chave):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == chave:
            return meio
        elif lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1

    return inicio


def contar_elementos_no_intervalo(lista, X, Y):
    # Trata caso onde o intervalo é inválido
    if X > Y:
        return 0

    # k1: índice do primeiro elemento >= X
    k1 = busca_binaria_ponto_insercao(lista, X)

    # k2: índice do primeiro elemento > Y (usando Y + 1)
    k2 = busca_binaria_ponto_insercao(lista, Y + 1)

    # A quantidade de elementos no intervalo [X, Y] é a diferença dos pontos de inserção
    return k2 - k1


dados = [10, 20, 30, 40, 50, 60, 70, 80]

# Exemplo 1: Elementos entre 25 e 65 (30, 40, 50, 60 -> 4 elementos)
print(contar_elementos_no_intervalo(dados, 25, 65))  # Output: 4

# Exemplo 2: Limites exatos contidos na lista (20 a 50 -> 20, 30, 40, 50 -> 4 elementos)
print(contar_elementos_no_intervalo(dados, 20, 50))  # Output: 4

# Exemplo 3: Intervalo fora da lista (1 a 5)
print(contar_elementos_no_intervalo(dados, 1, 5))  # Output: 0

# Exemplo 4: Intervalo que abrange toda a lista (0 a 100)
print(contar_elementos_no_intervalo(dados, 0, 100))  # Output: 8
