"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint as rd
from time import sleep as sp

jogos = int(input("Quantos jogos? "))
num_sorteados = []
for i in range(jogos):
    for p in range(6):
        p = rd(1,60)
        if len(num_sorteados) == 0:
            num_sorteados.append(p)
        else:
            while p in num_sorteados:
                p = rd(1,60)
            num_sorteados.append(p)
    num_sorteados.sort()
    print(f"Jogo {i+1}: {num_sorteados}")
    num_sorteados.clear()
    sp(1.3)
print("Boa sorte!")
