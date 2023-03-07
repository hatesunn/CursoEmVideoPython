"""
Melhore o jogo do EX028 onde o computador vai "pensar em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
"""

from random import randint
from time import sleep

cpu = randint(0, 10)
tentativas = 1
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
print("-=-" * 20)
jogador = int(input("Em que número pensei? "))
while jogador > 10 or jogador < 0:
    jogador = int(input("Número digitado inválido. Por favor, digite um número entre 0 e 10: "))
print("Processando...")
sleep(1.3)
while jogador != cpu:
    print("\033[31mNúmero errado\033[m.")
    # print(cpu) # cheater
    novo = input("Tentar novamente (S/N)? ").upper()
    while novo != "S":
        novo = input("Opção inválida. Deseja tentar novamente (S/N)? ").upper()
    if novo == "S":
        tentativas += 1
        jogador = int(input("Em que número pensei? "))
        while 0 > jogador > 10 :
            jogador = int(input("Número digitado inválido. Por favor, digite um número entre 0 e 10: "))
    else:
        print(f"Você saiu com {tentativas} tentativas.")
        exit()
print("\033[32mAcertou o número! Parabéns\033[m")
print(f"Voce acertou com {tentativas} tentativas.")
