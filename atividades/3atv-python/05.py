
nome = input("Digite seu nome (mais de 3 caracteres): ")
while len(nome) <= 3:
    print("Erro: O nome deve ter mais de 3 caracteres.")
    nome = input("Digite o nome novamente: ")


idade = int(input("Digite sua idade (0 a 100): "))
while idade < 0 or idade > 100:
    print("Erro: A idade deve estar entre 0 e 100.")
    idade = int(input("Digite a idade novamente: "))


salario = float(input("Digite seu salário (maior que 0): "))
while salario <= 0:
    print("Erro: O salário deve ser maior que zero.")
    salario = float(input("Digite o salário novamente: "))


sexo = input("Sexo ('f' ou 'm'): ").lower()
while sexo != 'f' and sexo != 'm':
    print("Erro: Digite apenas 'f' ou 'm'.")
    sexo = input("Sexo ('f' ou 'm'): ").lower()


estado_civil = input("Estado Civil ('s', 'c', 'v', 'd'): ").lower()
while estado_civil not in ['s', 'c', 'v', 'd']:
    print("Erro: Use 's', 'c', 'v' ou 'd'.")
    estado_civil = input("Estado Civil ('s', 'c', 'v', 'd'): ").lower()

print("\nCadastro Concluído")
print(f"Nome: {nome} | Idade: {idade} | Salário: {salario} | Sexo: {sexo} | Estado Civil: {estado_civil}")