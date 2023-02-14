"""
Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e
mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
"""
s = 0
for c in range(0,6):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        s += n
print(f"A soma dos números pares dos números digitados é: \033[32m{s}\033[m.")
