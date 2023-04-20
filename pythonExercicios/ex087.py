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
print(f"""
[ {num[0][0]} ] [ {num[0][1]}  ] [ {num[0][2]} ]
[ {num[1][0]} ] [ {num[1][1]}  ] [ {num[1][2]} ]
[ {num[2][0]} ] [ {num[2][1]}  ] [ {num[2][2]} ]
"""
)
print(f"A soma dos números pares é: {par}")
soma = num[0][2] + num[1][2] + num[2][2]
print(f"A soma dos números na 3ª coluna é: {soma}")
if num[2][1] < num[0][1] > num[1][1]:
    maior = num[0][1]
elif num[0][1] < num[1][1] > num[2][1]:
    maior = num[1][1]
else:
    maior = num[2][1]
print(f"O maior número na 2ª coluna é: {maior}")