# Exercício proposto retirado do site: https://www.pythonprogressivo.net/2018/02/Exercicios-Python-IF-ELIF-ELSE.html
#
#3. Faça um Programa que leia três números inteiros e mostre o maior deles.

# Leitura de dados
num1 = int(input("Digite 3 números: \n"
                "1- "))
num2 = int(input("2- "))
num3 = int(input("3- "))

# Primeiro jeito

# if num3 < num1 > num2:
#     print(f"O número maior é: 1- {num1}")
# elif num1 < num2 > num3:
#     print(f"O número maior é: 2- {num2}")
# else:
#     print(f"O número maior é: 3- {num3}")

# Segundo jeito (ídeia capturado do site)

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
print("O número maior é: ",maior)
