"""
Faça um programa que leia 5 valores numéricos e guarde-os em um lista.
N final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

lista = []
max = min = 0
for l in range(5):
    lista.append(int(input(f"Digite número na posição {l}: ")))
    if l == 0:
        max = min = lista[l]
    else:
        if lista[l] > max:
            max = lista[l]
        if lista[l] < min:
            min = lista[l]
print(f"Os números digitados foram: {lista}")
print(f"O maior número foi {max} nas posições: ", end="")
for i, v in enumerate(lista):
    if v == max:
        print(f"{i}...", end="")
print()
print(f"O menor número foi {min} nas posições: ", end="")
for i, v in enumerate(lista):
    if v == min:
        print(f"{i}...", end="")
print()