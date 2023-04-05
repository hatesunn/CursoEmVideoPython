"""
Crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

tabela = ("Café", 3, "Chocolate", 5.50, "Pão na chapa", 2.50)
print("-"*58)
print("{:^60}".format(" Tabela de preços "))
print("-"*58)
print(f"""
{tabela[0]}...............................................R$ {tabela[1]:.2f}
{tabela[2]}..........................................R$ {tabela[3]:.2f}
{tabela[4]}.......................................R$ {tabela[5]:.2f}
""")