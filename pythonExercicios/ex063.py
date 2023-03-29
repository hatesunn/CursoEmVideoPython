"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequencia de Fibonacci.
Ex:
0 - 1 - 1 -2 -3 -5 -8
"""

n = int(input("Digite um número: "))
s = 0
a1 = 0
a2 = 1
a3 = 1
while s < n:
    s += 1
    if s == n:
        print(a3, end=".")
    else:
        print(a3, end=", ")
    a3 = a1 + a2
    a1 = a2
    a2 = a3
