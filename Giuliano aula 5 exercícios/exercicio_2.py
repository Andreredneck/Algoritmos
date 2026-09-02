def busca_binaria_ponto_insercao(lista, chave):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == chave:
            return meio  # Caso 1: A chave foi encontrada exatamente no índice 'meio'
        elif lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1

    # Caso 2: A chave não está na lista.
    # O ponteiro 'inicio' estará exatamente na posição 'k' apropriada.
    return inicio


dados = [10, 20, 30, 40, 50]  # n = 5 elementos (índices 0 a 4)

# 1. Elemento presente na lista
print(busca_binaria_ponto_insercao(dados, 30))  # Retorna: 2 (lista[2] == 30)

# 2. Inserção no meio (entre k-1 e k)
print(busca_binaria_ponto_insercao(dados, 25))  # Retorna: 2 (insere entre 20 e 30)

# 3. Inserção antes da primeira posição (k = 0)
print(busca_binaria_ponto_insercao(dados, 5))  # Retorna: 0 (insere antes do 10)

# 4. Inserção após a última posição (k = n = 5)
print(busca_binaria_ponto_insercao(dados, 60))  # Retorna: 5 (insere depois do 50)
