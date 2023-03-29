"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
e qual fo o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
"""

num = int(input("Digite um número: "))
n1 = num
qtd = 1
menor = maior = num
cont = input("Deseja continuar(S/N)? ").upper()
while cont != "S" and cont != "N":
    cont = input("Opção inválida. Deseja continuar(S/N)? ").upper()
while cont == "S":
    num = int(input("Digite outro número: "))
    n1 = n1 + num
    qtd += 1
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    cont = input("Deseja continuar(S/N)? ").upper()
    while cont != "S" and cont != "N":
        cont = input("Opção inválida. Deseja continuar(S/N)? ").upper()
media = n1 / qtd
print(f"A média dos valores digitados é: {media:.2f}. O menor número foi {menor} e o maior foi {maior}.")

