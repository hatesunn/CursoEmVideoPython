"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados;
B) A lista de valores, ordenada em forma decrescente;
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = []
c = 0
while c != 2:
    if c == 2:
        break
    n = int(input("Digite um número: "))
    lista.append(n)
    while True:
        c = int(input("""
Deseja adicionar outro número?
[1] Sim
[2] Não
"""))
        if c == 1 or c == 2:
            break
        else:
            print("Opção inválida!")
print(f"Os números digitados foram: {lista}")
print(f"A quantidade de números digitados foram {len(lista)}")
inv = lista[:]
inv.sort(reverse=True)
print(f"A lista ordenada em forma decrescente é: {inv}")
if 5 in lista:
    print(f"O número 5 foi digitado na posição: {lista.index(5)}")
else:
    print("O número 5 não foi digitado.")
