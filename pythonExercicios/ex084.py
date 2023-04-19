"""
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas;
B) Uma listagem com as pessoas mais pesadas;
C) Uma listagem com as pessaos mais leves.
"""

lista = []
pesadas = []
leves = []
pessoas = 0
while True:
    nome = input("Digite o nome: ")
    peso = int(input("Digite o peso: "))
    lista.append((nome, peso))
    pessoas += 1
    if len(lista) == 1:
        pesadas.append(lista[0])
        leves.append(lista[0])
    else:
        if peso > pesadas[0][1]:
            pesadas = [(nome, peso)]
        elif peso == pesadas[0][1]:
            pesadas.append((nome, peso))
        if peso < leves[0][1]:
            leves = [(nome, peso)]
        elif peso == leves[0][1]:
            leves.append((nome, peso))
    while True:
        c = input("Deseja adicionar outro?[S/N] ").upper().strip()[0]
        if c in 'SN':
            break
        else:
            print("Opção inválida!")
    if c == "N":
        break
print("-=" * 30)
print(f"Total de pessoas cadastradas: {pessoas}")
print("Pessoas mais pesadas:")
for nome, peso in pesadas:
    print(f"{nome} ({peso} kg)")
print("Pessoas mais leves:")
for nome, peso in leves:
    print(f"{nome} ({peso} kg)")