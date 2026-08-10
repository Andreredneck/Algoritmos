# Leitura do número inteiro
numero = int(input("Digite um número inteiro: "))

print(f"\nTabuada do {numero}:")

# Estrutura de repetição de 1 a 10
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")