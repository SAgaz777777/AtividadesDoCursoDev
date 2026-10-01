vendas = float(input("Digite o valor total das vendas: R$ "))
taxa_comissao = float(input("Digite a porcentagem da comissão: "))

comissao = (vendas * taxa_comissao) / 100

print("O valor da comissão a receber é: R$ {}".format(comissao))