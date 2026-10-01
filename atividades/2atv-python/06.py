print("Menu:\n1: Pizza\n2: Hambúrguer\n3: Salada")
opcao = input("Escolha uma opção (1-3): ")

match opcao:
    case "1":
        print("Você selecionou: Pizza")
    case "2":
        print("Você selecionou: Hambúrguer")
    case "3":
        print("Você selecionou: Salada")
    case _:
        print("Opção inválida.")

     