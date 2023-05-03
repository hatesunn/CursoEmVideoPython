"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
0[][][]
1[][][]
2[][][]
 0 1 2
No final, mostre a matriz com a formatação correta
"""

num = [[],[],[]]
x = 0
for i in range(3):
    for i in range(3):
        i = int(input(f"Digite um valor para [{x}, {i}]: "))
        num[x].append(i)
    x += 1
for l in range(0,3):
    for c in range(0,3):
        print(f"[{num[l][c]:^5}]", end="")
    print()
