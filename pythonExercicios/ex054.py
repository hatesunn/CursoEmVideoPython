"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
Maioridade = 21 anos.
"""
from datetime import date as dt

maior = 0
menor = 0
hj = dt.today().year
for a in range(0, 8):
    ano = int(input("Digite seu ano de nascimento: "))
    if ano <= (hj - 21):
        maior += 1
    else:
        menor += 1
print(f"{maior} maioridade e {menor} menoridade.")