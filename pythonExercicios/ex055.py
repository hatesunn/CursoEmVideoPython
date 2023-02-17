"""
Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o Maior peso e o Menor peso lidos.
"""

maior = 0
menor = 0
for p in range(0, 5):
    peso = float(input("Digite seu peso(KG): "))
    if peso > maior:
        maior = peso
    elif peso < menor or menor == 0:
        menor = peso
print(f"O maior peso é {maior}kg e o menor é {menor}kg.")
