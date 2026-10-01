dia = input("Digite o dia da semana (ex: Sábado, Segunda): ").strip().capitalize()

match dia:
    case "Segunda" | "Terça" | "Quarta" | "Quinta" | "Sexta":
        print(f"{dia} é um dia útil.")
    case "Sábado" | "Domingo":
        print(f"{dia} é fim de semana.")
    case _:
        print("Dia inválido.")