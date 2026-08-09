# Lendo os dois números 

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizando as operações matemáticas

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Não é possível dividir por zero"

# Resultados 

print(f"A soma de {num1} e {num2} é: {soma}")
print(f"A subtração de {num1} e {num2} é: {subtracao}")
print(f"A multiplicação de {num1} e {num2} é: {multiplicacao}")



