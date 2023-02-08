# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# até 9 : Mirim
# até 14: Infantil
# até 19: Junior
# até 20: Sênior
# acima Master

# import do ano atual
from datetime import date
hj = date.today()
ano = hj.year

# Entrada do ano do usuário
nascimento = int(input("Digite seu ano de nascimento(AAAA): "))

# Saída
idade = ano - nascimento
print(f"Sua idade é: {idade}")
print
if idade <= 9:
    print("Sua categoria é : Mirim")
elif 14 >= idade >9:
    print("Sua categoria é: Infantil")
elif 19 >= idade >14:
    print("Sua categoria é: Junior")
elif 20 == idade:
    print("Sua categoria é: Senior")
else:
    print("Sua categoria é: Master")
