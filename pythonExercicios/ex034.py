# Escreva um programa que pergutnte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a 1250,00, calcule um aumento de 10%
# para os inferiores ou iguais, o aumento é de 15.

sal = float(input("Digite seu salário atual: R$"))
if sal <= 1250:
    sal = sal * 1.15
    print(f"Seu novo salário será de: R$ {sal:.2f}")
else:
    sal = sal * 1.10
    print(f"Seu novo salário será de: R$ {sal:.2f}")
