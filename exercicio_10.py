numeros = []

# Laço para receber 5 números 

for i in range(1,6):
    num = float(input(f"Digite o {i}º número: "))
numeros.append(num)

# Identificador de maior e menor número

maior = max(numeros)
menor = min(numeros)

print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")
