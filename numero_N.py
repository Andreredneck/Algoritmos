# Leitura do número N
N = int(input("Digite um número N: "))

# Variável para acumular a soma
soma = 0

# Somando de 1 até N
for i in range(1, N + 1):
    soma += i

# Exibição do resultado
print(f"A soma dos números de 1 até {N} é: {soma}")