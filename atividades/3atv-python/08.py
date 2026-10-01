# Inicializa a lista de 1 até 10
numeros = list(range(1, 11))

print("Números pares da lista:")
for n in numeros:
    if n % 2 == 0: # Verifica se o resto da divisão por 2 é zero
        print(n)