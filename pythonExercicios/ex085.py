"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
par = []
impar = []
lista = [par, impar]
for n in range(7):
    num = int(input(f"Digite o {n+1} número: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
par.sort()
impar.sort()
print(lista)
print(f"Os números pares digitados foram: {par}")
print(f"Os números ímpares digitadso foram: {impar}")