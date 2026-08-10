soma = 0 

while True:
    numero = float(input("Digite um número (ou digite 0 para sair): "))
    if numero == 0:
        break
    soma += numero  #Acumula os números digitados
    
    print(f"A soma dos números digitados até agora é: {soma}")
    