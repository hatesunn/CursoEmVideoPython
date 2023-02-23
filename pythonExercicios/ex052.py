"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
t =0
n = int(input("Digite um número: "))
for c in range(1, n+1):
    if n % c == 0:
        print("\033[33m", end=" ")
        t += 1
    else:
        print("\033[31m", end=" ")
    print(c, end=" ""\033[m")
print(f"\nO número {n} foi dívisel {t} vezes.")
if t == 2:
    print("E por isso ele é PRIMO!")
else:
    print("E por isso ele NÃO é PRIMO!")
