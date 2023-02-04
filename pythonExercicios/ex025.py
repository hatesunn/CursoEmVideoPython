# Crie um programa que leia o nome de uma pessao e diga
# se ela tem "Silva" no nome

# nome = str(input('Digite seu nome: ')).strip()
# silva = 'Silva' in nome.title()
#
# if silva:
#     print('Tem Silva no nome.')
# else:
#     print('Não tem Silva no nome.')

# Outra forma

nome = str(input('Digite seu nome: ')).strip()
print(f'Seu nome tem silva {"silva" in nome.lower()}')
