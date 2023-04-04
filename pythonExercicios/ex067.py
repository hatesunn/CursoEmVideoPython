"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""

while True:
    n = int(input("\nDigite um número: "))
    if n < 0:
        break
    for t in range(11):
        print(f"{n} x {t} = {n*t}")
print("Encerrando...")
