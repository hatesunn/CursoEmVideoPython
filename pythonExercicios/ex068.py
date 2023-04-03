"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

import random
vitorias = 0
while True:
    n = int(input("Digite um valor: "))
    par_impar = str(input("Você quer par ou ímpar? ")).upper()
    par_impar = par_impar[0]
    cpu = random.randint(1,2)
    soma = n + cpu
    print(cpu)
    if soma % 2 == 1:
        resultado = 1 #impar
    else:
        resultado = 0 #par
    if resultado == 1 and par_impar == "I":
        print("\033[32mAcertou!\033[m")
        vitorias += 1
    elif resultado == 0 and par_impar == "P":
        print("\033[32mAcertou!\033[m")
        vitorias += 1
    elif resultado == 1 and par_impar == "P":
        print("\033[31mErrou!\033[m")
        break
    elif resultado == 0 and par_impar == "I":
        print("\033[31mErrou!\033[m")
        break
print(f"Voce teve {vitorias} vitórias seguidas.")