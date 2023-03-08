"""
Crie um programa que leia DOIS VALORES e mostre um MENU na tela:
[1] somar
[2] multiplicar
[3] Maior
[4]Novos números
[5]Sair
"""

import time
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
menu = 0
while menu != 5:
    menu = int(input("""\nO que você deseja fazer?
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos número
[5] Sair
"""
))
    while menu > 5:
       print("\033[31mOpção inválida.\033[m")
       menu = int(input("""O que você deseja fazer?
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos número
[5] Sair
"""
))
    if menu == 1:
        print(f"A soma dos valores é {num1 + num2}.")
    elif menu == 2:
        print(f"A multiplicação dos valores é {num1 * num2}.")
    elif menu == 3:
        if num1 > num2:
            print(f"O maior número é {num1}.")
        else:
            print(f"O maior número é {num2}.")
    elif menu == 4:
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
print("Saindo...")
time.sleep(1.3)
exit()
