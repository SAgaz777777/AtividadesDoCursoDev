soma = 0
valido = True

for i in range(1, 5):
    nota = float(input(f"Digite a nota {i}: "))
    
   
    if 0 <= nota <= 10:
        soma += nota
    else:
      
        print(f"Erro: A nota {nota} é inválida! Digite apenas valores de 0 a 10.")
        valido = False
        


if valido:
    media = soma / 4
    print(f"Média final: {media}")