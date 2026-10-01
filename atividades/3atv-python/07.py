while True:
    print("\n--- MENU DE OPÇÕES ---")
    print("1 - Eu programo em Python")
    print("2 - Eu programo em PHP")
    print("3 - Eu programo em Java")
    
    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    if opcao == "1":
        print("Mensagem: Você está no caminho da Inteligência Artificial com Python!")
        break
    elif opcao == "2":
        print("Mensagem: PHP é o motor da web dinâmica!")
        break
    elif opcao == "3":
        print("Mensagem: Java é robusto e está em bilhões de dispositivos!")
        break
    else:
        print("Opção inválida! Tente novamente.")