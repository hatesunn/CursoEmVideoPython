"""
Aprimore o desafio anterior, mostrando:
A) A soma de todos os valores pares digitados;
B) A soma dos valores da terceira coluna;
C) O maior valor da segunda linha.
"""

num = [[],[],[]]
x = par = maior = 0
for i in range(3):
    for i in range(3):
        i = int(input(f"Digite um valor para [{x}, {i}]: "))
        if i % 2 == 0:
            par += i
        num[x].append(i)
    x += 1
for l in range(0,3):
    for c in range(0,3):
        print(f"[{num[l][c]:^5}]", end="")
    print()
print(f"A soma dos números pares é: {par}")
soma = num[0][2] + num[1][2] + num[2][2]
print(f"A soma dos números na 3ª coluna é: {soma}")
for c in range(0,3):
    if c == 0:
        maior = num[1][c]
    elif num[1][c] > maior:
        maior = num[1][c]
print(f"O maior número na 2ª linha é: {maior}")