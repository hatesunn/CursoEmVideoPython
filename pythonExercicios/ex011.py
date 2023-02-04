# Faça um programa que leia a largura
# e a altura de uma parede em metros,
# calcule a sua área de a quantidade de
# tinta necessária para pintá-lo, sabendo que
# cada litro de tinta pinta uma 2m²

print('-'*15)
print('-- Calculando quantos litros de tinta necessário --')
lar = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))

print(f'O tamanho da parede é {lar * alt:.2f} m²\n'
      f'É necessário ultilizar {(lar * alt) /2:.2f} lts de tinta')
