# Crie um programa que leia um número inteiro e mostre
# se ele é PAR ou ÍMPAR.

num = int(input("Digite um número: "))
if (num % 2) == 1:
    print(f"O número digitado é {num}. Ele é ímpar.")
else:
    print(f"O número digitado é {num}. Ele é par.")
