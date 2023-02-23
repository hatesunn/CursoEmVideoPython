"""
Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

print("-="*10,"Progressão Aritmética","-="*10)
a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
for c in range(a1, a1+(10-1)*r , r):
    print(c, end="-> ")
print("Acabou")