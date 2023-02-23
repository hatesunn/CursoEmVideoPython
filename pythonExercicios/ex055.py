"""
Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o Maior peso e o Menor peso lidos.
"""

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f"Digite o peso da {p}ª pessoa: "))
    if peso > maior:
        maior = peso
    elif peso < menor or menor == 0:
        menor = peso
print(f"O maior peso é {maior}kg e o menor é {menor}kg.")
