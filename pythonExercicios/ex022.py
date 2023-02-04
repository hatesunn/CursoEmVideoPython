# Crie um programa que leia o nome completo de uma pessoa e mostre
# 1- nome com todas as letras maiúsculas
# 2- O nome com todas minúsculas
# 3- Quantas letras ao todo(considerar os espaços)
# 4 - Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
pnome = nome.split()
print(f'Nome com letras maiúsculas é {nome.upper()}.')
print(f'Nome com letras minúsculas é {nome.lower()}.')
print(f'Quantidades de carácteres é {len(nome) - nome.count(" ")} ')
print(f'O primeiro nome tem {len(pnome[0])}')
# Outra variação:
# print(f'O primeiro nome tem {nome.find(" ")}')


