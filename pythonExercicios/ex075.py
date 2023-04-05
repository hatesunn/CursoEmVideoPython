"""
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final mostre:
A) Quantas vezes apareceu o valor 9;
B) Em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares.
"""

n = ()
par = ()
for i in range(4):
    x = int(input("Digite um número: "))
    if x % 2 == 0:
        par += tuple([x])
    n += (x,)
print(f"Você digitou os números: {n}")
print("A) Quantas vezes apareceu o valor 9?")
if 9 in n:
    print(f"O número 9 aparece {n.count(9)} vezes.")
else:
    print("Não possui o número 9.")
print("B) Em que posição foi digitado o primeiro valor 3?")
if 3 in n:
    print(f"O número 3 foi digitado na {n.index(3)+1}ª posição.")
else:
    print("Não possui o número 3.")
print("c) Quais foram os números pares?")
if par == 0:
    print("Não possui nenhum número par.")
else:
    print(f"Os números pares foram {par}")
print("Finalizando...")
