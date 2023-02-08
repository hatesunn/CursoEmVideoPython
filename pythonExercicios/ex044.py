# Elabore um programa que calcule o valor a ser pago por um produto
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

# Coleta de dados
valor = float(input("Digite o valor do produto: R$"))
pag = int(input("Qual a forma de pagamento? \n"
                "[1] Dinheiro ou cheque\n"
                "[2] Débito ou crédito à vista\n"
                "[3] Parcelado em 2x s/ juros\n"
                "[4] Parcelado em 3x c/ juros\n"))
while 4 < pag :
    print("Forma de pagamento errado. Por favor, digite um número entre 1 e 4.")
    pag = int(input("Qual a forma de pagamento? \n"
                "[1] Dinheiro ou cheque\n"
                "[2] Débito ou crédito à vista\n"
                "[3] Parcelado em 2x s/ juros\n"
                "[4] Parcelado em 3x c/ juros\n"))
# Saída
print(f"O valor do produto é: {valor:.2f} ")
if pag == 1:
    print(f"A forma de pagameto é Dinheiro/Cheque. Valor do final é {valor * .9:.2f}")
elif pag == 2:
    print(f"A forma de pagamento é Débito/Crédito à vista. Valor final é {valor * .95:.2f}")
elif pag == 3:
    print(f"A forma de pagamento é Parcelado em 2x. O valor de cada parcela é {valor /2:.2f}")
elif pag == 4:
    print(f"A forma de pagamento é Parcelado em 3x. O valor de cada parcela é {(valor * 1.20)/3:.2f}")
