# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 peça para o usuário tentar descobrir
# qual foi o núemro escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
#
# num = int(input("Digite um número entre 0 e 5, para tentar adivinhar qual número correto: "))
# while num > 5:
#     num = int(input("Número inválido. Por favor digite um número entre 0 e 5: "))
# if num == 4:
#     print("Parabéns! Você acertou o número.")
# else:
#     print("Desculpe, o número digitado não é o correto")

from random import randint
from time import sleep

cpu = randint(0, 5)  # faz o cpu pensar
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? "))  # jogador tenta adivinhar
print("Processando...")
sleep(1.3)
if jogador == cpu:
    print("Parabéns! Você conseguiu acertar!")
else:
    print(f"Ganhei! Eu pensei no número {cpu} e não no {jogador}")
