"""
Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de
fogos de artifício, indo de 10 até 0, com uma pausa de 1s entre eles.
"""
from time import sleep as sp
from emoji import emojize as emo
n = 0
for c in range(10, 0, -1):
    print(f"{c}...")
    sp(1)
print(emo(':tada:', language='alias'))
