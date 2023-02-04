# Faça um programa que leia uma frase e pelo teclado e mostre:
# 1- Quantas vezes aparece a letra "A".
# 2- Em que posição ela aparece a primeira vez
# 3- Em que posição ela aparece a última vez.

# frase = input('Digite uma frase: \n')
# qtd = frase.upper().count('A')
# primeiro = frase.upper().find('A')
# ultimo = frase.split(-1)
# # ultimo = frase[-1]
# print(f'A quantidade de A na frase é : {qtd}.\n'
#       f'A primeira vez que aperece a letra A é no bloco: {primeiro}.\n'
#       f'A última vez que aperece a letra A é no bloco {ultimo}.')

# Correção

frase = str(input("Digite uma frase: ")).upper().strip()
print(f"A letra A aparece {frase.count('A')}")
print(f"A primeira A apareceu na posição {frase.find('A')+1}")
print(f"A última letra A apareceu na posição {frase.rfind('A')+1}")
