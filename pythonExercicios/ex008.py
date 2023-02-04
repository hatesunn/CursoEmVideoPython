# Escreva um programa que leia um valor
# em metroes e exiba convertido em
# centimetros e milimetros.

mt = float(input('Digite quantos metros: '))

print(f'A medida em centimetros é {int(mt * 100)} cm\n'
      f'A medida em milimetros é {int(mt * 1000)} mm')
