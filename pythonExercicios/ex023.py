# Faça um programa que leia um número de 0 a 9999 e mostre
# na tela um dos dígitos separados.
# Ex.: Digite um número: 1834
# unidades: 4 / dezenas: 3 / Centena: 8 / Milhar: 1

n = int(input('Digite um número entre 0 e 9999: '))
num = str(n)
while len(num) > 4:
    num = input('Número maior que 9999, por favor digite um número entre 0 e 9999: ')
print(f'O número digitado foi: {num}')
num = '000' + num
un = num[-1]

print(f'Contém: \n'
      f'Unidades: {un}\n'
      f'Dezenas: {num[-2]}\n'
      f'Centenas: {num[-3]}\n'
      f'Milhar: {num[-4]}')

# num = int(input('Informe um número: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print(f'Analisando o número {num}: \n'
#       f'Unidade: {u} \n'
#       f'Dezena: {d} \n'
#       f'Centena: {c} \n'
#       f'Milhar: {m} \n')