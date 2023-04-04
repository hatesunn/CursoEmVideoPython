"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag).
"""

s = c = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
    c += 1
print(f"A quantidade de números digitados foi {c} e a soma entre eles é {s}.")
