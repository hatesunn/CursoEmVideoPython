"""
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final mostre:
A) Quantas vezes apareceu o valor 9;
B) Em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares.
"""

n = impar = ()
for i in range(4):
    x = int(input("Digite um número: "))
    n += tuple([x])
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
for p in n:
    if p % 2 == 0:
        print(p, end=" ")
print("\nFinalizando...")
