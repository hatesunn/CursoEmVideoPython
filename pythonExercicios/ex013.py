# Faça um algoritmo que leia o salário de um
# funcionário e mostre seu novo salário
# com 15% de aumento.

print('-'*20)
print('-- Calculando um novo aumento pro funcionário --')

sal = float(input('Digite o valor do sálario atual: \n'
                  'R$ '))

porc = (sal + (sal * 15/100))

print(f'O novo sálario será de {porc:.2f}')

print('-'*20)