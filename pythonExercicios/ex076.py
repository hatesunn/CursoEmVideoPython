"""
Crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

tabela = ("Café", 3, "Chocolate", 5.50, "Pão na chapa", 2.50)
print("-"*58)
print("{:^60}".format(" Tabela de preços "))
print("-"*58)
for pos in range(0, len(tabela)):
    if pos % 2 == 0:
        print(f"{tabela[pos]:.<49}", end="")
    else:
        print(f"R${tabela[pos]:>7.2f}")