"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digigar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles.
(desconsiderando o flag(999).
"""

n = int(input("Digite um número(999 para parar): "))
vlr = qtd = 0
while n != 999:
    vlr += n
    qtd += 1
    n = int(input("Digite um número(999 para parar): "))
print(f"Foram digitados {qtd} números até o número 999. A soma total desses números é {vlr}.")
