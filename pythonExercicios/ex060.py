"""
Faça um programa que leia um número qualquer e mostre seu fatorial.
ex:
5! = 5x4x3x2x1=120
"""

num = int(input("Digite um número para calcular seu numero fatorial: "))
n1 = num
fat = num -1
n = 1
if num <= 1:
    print(f"O número fatorial de {num} é 1.")
else:
    while n < n1:
        n += 1 
        num *= fat
        fat -= 1
print(num)
