#variáveis

soma = 0
quantidade = 10

#leitura dos números
for i in range(1, quantidade + 1):
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero  #Acumula os números digitados
    
    #Cálculo da média
media = soma / quantidade

#resultados

print(f"A soma dos números digitados é: {soma}")
print(f"A média dos números digitados é: {media}")  
    