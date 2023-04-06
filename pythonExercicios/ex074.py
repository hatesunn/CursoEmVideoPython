"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma Tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
valor que estão na tupla.
"""

from random import randint
num = ()
for n in range(5):
    f = randint(0,10)
    num += (f,)

print(f"5 numeros aleatórios: {num}")
print(f"O menor número é : {min(num)}")
print(f"O maior número é : {max(num)}")
