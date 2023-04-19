"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final mostre o conteúdo das três listas geradas.
"""

lista = []
lista_par = []
lista_impar = []
c = 1
while True:
    if c == 2:
        break
    n = int(input("Digite um número: "))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    while c != 2:
        c = int(input("""
Deseja adicionar outro número?
[1]Sim
[2]Não
"""))
        if c == 1:
            break
print(f"A lista de números digitados foram:\n{lista}")
print(f"Lista de números ímpares:\n{lista_impar}")
print(f"Lista de números pares:\n{lista_par}")
    