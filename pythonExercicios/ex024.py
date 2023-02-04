# Crie um programa que leia o nome de uma cidade e diga
# se ela começa ou não com o nome "Santo".

# nome = str(input('Digite nome da cidade: ')).strip()
# nome = nome.lower()
# verifica = nome[:5]
# if verifica == 'santo':
#     print('Possui')
# else:
#     print('Não possui')

# Outra forma de fazer:

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')


