"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

import random
vitorias = 0
while True:
    n = int(input("Digite um valor: "))
    par_impar = " "
    while par_impar not in "PI":
        par_impar = str(input("Você quer par ou ímpar? ")).strip().upper()[0]
    cpu = random.randint(1,2)
    soma = n + cpu
    if par_impar == "P":
        if soma % 2 == 0:
            print("\033[32mAcertou!\033[m")
            vitorias += 1
        else:
            print("\033[31mErrou!\033[m")
            break
    if par_impar == "I":
        if soma % 2 == 1:
            print("\033[32mAcertou!\033[m")
            vitorias += 1
        else:
            print("\033[31mErrou!\033[m")
            break
print(f"Voce teve {vitorias} vitórias seguidas.")
