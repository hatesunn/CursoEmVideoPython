 # Escreva um programa que leia 2 números inteiros e compare-os, mostrando na tela uma mensagem:
 # O primeiro valor é maior
 # O segundo valor é maior
 # Não existe valor maior, os dois são iguais.

# leitura de dados
num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
print(f"O primeiro valor digitado é {num1} e o segundo é {num2}.\n")

# resultado
if num1 > num2:
    print(f"O primeiro valor({num1}) é maior.")
elif num2 > num1:
    print(f"O segundo valor({num2}) é maior.")
else:
    print("Não existe valor maior. Os 2 são iguais.")
