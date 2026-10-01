soma_geral = 0

for i in range(1, 4):
    print(f"{"=" * 5} Soma {i} {"=" * 5}")
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    
    soma_atual = n1 + n2
    print(f"Resultado da soma {i}: {soma_atual}\n")
    
 
    soma_geral+=soma_atual

print("")
print(f"Total (Soma de todos os resultados): {soma_geral}")