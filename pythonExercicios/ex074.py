"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma Tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
valor que estão na tupla.
"""

from random import randint
a = randint(0,10)
b = randint(0,10)
c = randint(0,10)
d = randint(0,10)
e = randint(0,10)
f = (a , b, c, d, e)
print(f"5 numeros aleatórios: {f}")
print(f"O menor número é : {min(f)}")
print(f"O maior número é {max(f)}")