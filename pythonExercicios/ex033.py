# Faça um programa que leia três números e mostre
# qual é o maior e qual é o menor.

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))
# num3 = int(input("Digite mais um número: "))
#
# if num3 < num1 > num2:
#     print(f"O maior número é {num1}")
# else:
#     if num3 < num2 > num1:
#         print(f"O maior número é {num2}")
#     else:
#         print(f"O maior número é {num3}")
#
# if num3 > num1 < num2:
#     print(f"O menor número é {num1}")
# else:
#     if num3 > num2 < num1:
#         print(f"O menor número é {num2}")
#     else:
#         print(f"O menor número é {num3}")

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))
# verificar menor número
menor = n1
if n3 > n2 < n1:
    menor = n2
if n2 > n3 < n1:
    menor = n3
# verificar o maior número
maior = n1
if n3 < n2 > n1:
    maior = n2
if n2 < n3 > n1:
    maior = n3

print(f"O menor valor digitado é {menor}")
print(f"O maior valor digitado é {maior}")
