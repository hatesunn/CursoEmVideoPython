"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai 
continuar. No final, mostre:
A)Qual é o total gasto na compra;
B)Quantos produtos custam mais de R$1000;
C)Qual é o nome do produto mais barato.
"""
total = prod_1k = mais_barato = 0
barato = ""
while True:
    prod_nome = str(input("Produto: "))
    prod_preco = float(input("Preço: "))
    if prod_preco > 1000:
        prod_1k += 1
    if barato == "" or prod_preco < mais_barato:
        barato = prod_nome
        mais_barato = prod_preco
    total += prod_preco

    cont = str(input("Deseja continuar(S/N)? ")).upper()
    cont = cont[0]
    if cont == "N":
        break
print(f"O total gasto da compra foi {total:.2f}, {prod_1k} produtos custam mais de 1000,00 e o produto mais barato é {barato}({mais_barato:.2f}).")