# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar
# Se já paassou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou de prazo.


# # Entrada de dados
# ano = int(input("Informe seu ano de nascimento: "))

# # Condicoes e saída
# if ano > 18:
#     print("Você já é de maior. Seu ano de alistamento já passou.")
#     if ano - 18 == 1:
#         print(f"Já faz {ano - 18} ano que passou seu alistamento.")
#     else:
#         print(f"Já fazem {ano - 18} anos que passou seu alistamento.")
# elif ano == 18:
#     print("Seu alistamento é esse ano.")
# else:
#     print(f"Você ainda é de menor.")
#     if 18 - ano == 1:
#         print(f"Ainda falta {18-ano} ano pra você se alistar.")
#     else:
#         print(f"Ainda faltam {18-ano} anos pra você se alistar.")
    
# Correção

from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc
print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}")
if idade == 18:
    print("Voce tem que se alistar esse ano!")
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f"Voce ainda é de menor. Ainda {saldo} anos para se alistar. Será em {ano}")
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f"Já passou o seu alistamento. Foram {saldo} anos atrás. Foi no ano de {ano}")
