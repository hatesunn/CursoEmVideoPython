"""
Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação novamente até ter o valor correto.
"""

sexo = str(input("Qual o seu sexo(M/F)? ")).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input("Sexo digitado inválido. Por favor digite novamente(M/F): ")).upper()
if sexo == "M":
    print("O sexo digitado é \033[34mMASCULINO\033[m")
else:
    print("O sexo digitado é \033[31mFEMININO\033[m")
