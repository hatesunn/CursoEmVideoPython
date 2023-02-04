# Faça um algoritmo que leia o preço
# de um produto e mostre seu novo preço
# com 5% de desconto.

print('-'*15)
print('-- Calculando valor de desconto --')

vlr = float(input('Digite o valor do produto:\n'
                  'R$ '))

print(f'Valor normal: R$ {vlr:.2f}\n'
      f'Valor à vista: R$ {(vlr - (vlr * 5/100)):.2f}')
