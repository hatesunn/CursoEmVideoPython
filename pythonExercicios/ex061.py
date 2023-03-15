"""
Refaca o ex051, lendo o PRIMEIRO TERMO e a RAZÃO de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura While
"""

print("-="*10,"Progressão Aritmética","-="*10)
a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
a10 = 0
while a10 < 10:
   print (a1, end="-> ")
   a1 = a1 + r
   a10 += 1
print("Acabou")