"""
Faça um programa que leia 5 valores numéricos e guarde-os em um lista.
N final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

lista = []
for l in range(5):
    n = int(input("Digite um número: "))
    lista.append(n)
print(f"Os números digitados foram: {lista}")
print(f"O maior número foi {max(lista)} na posição {lista.index(max(lista))}ª")
print(f"O menor número foi {min(lista)} na posição {lista.index(min(lista))}ª")
