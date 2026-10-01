nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 16:
    print(f"Olá {nome}, você já tem idade suficiente para votar!")
else:
    print(f"Olá {nome}, você ainda não pode votar.")