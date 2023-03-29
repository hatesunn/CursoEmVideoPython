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
# print(cpu) # - CHEAT -
jogador = int(input("Em que número pensei? "))
while jogador > 10 or jogador < 0:
    jogador = int(input("Número digitado inválido. Por favor, digite um número entre 0 e 10: "))
print("Processando...")
sleep(1.3)
if jogador == cpu:
    print("\033[32mIMPRESSIONANTE! Você acertou o número de primeira!! Muito bem! Parabéns!\033[m")
else:
    while jogador != cpu:
        print("\033[31mNúmero errado\033[m.")
        if jogador > cpu:
            print("Número é menor...")
        else:
            print("Número é maior...")
        novo = input("Tentar novamente (S/N)? ").upper()
        while novo != 'S' and novo != 'N':
            novo = input("Opção inválida. Deseja tentar novamente (S/N)? ").upper()
        if novo == "S":
            tentativas += 1
            jogador = int(input("Em que número pensei? "))
            while jogador > 10 or jogador < 0:
                jogador = int(input("Número digitado inválido. Por favor, digite um número entre 0 e 10: "))
            print("Processando....")
            sleep(1.3)
        else:
            if tentativas > 1:
                print(f"Que pena, você não acertou. Você saiu com {tentativas} tentativas.")
            else:
                print(f"Que pena, você não acertou. Você saiu com {tentativas} tentativa.")
    print("\033[32mAcertou o número! Parabéns!\033[m")
    print(f"Você acertou com {tentativas} tentativas.")
