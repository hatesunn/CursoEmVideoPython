"""
Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e
mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
"""
s = 0
for c in range(1,7):
    n = int(input(f"Digite o {c}º valor: "))
    if n % 2 == 0:
        s += n
print(f"A soma dos pares dos valores digitados é: \033[32m{s}\033[m.")
