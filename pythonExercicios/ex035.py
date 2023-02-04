# Desenvolva um programa que leia o comprimento de três
# e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input("Digite o tamanho do lado a: "))
b = float(input("Digite o tamanho do lado b: "))
c = float(input("Digite o tamanho do lado c: "))

if a + b > c and b + c > a and c + a > b:
    print("Forma-se um triângulo.")
else:
    print("Não forma.")
