# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar
# Se já paassou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou de prazo.

# Entrada de dados
ano = int(input("Informe sua idade: "))

# Condicoes e saída
if ano > 18:
    print("Você já é de maior. Seu ano de alistamento já passou.")
    if ano - 18 == 1:
        print(f"Já faz {ano - 18} ano que passou seu alistamento.")
    else:
        print(f"Já fazem {ano - 18} anos que passou seu alistamento.")
elif ano == 18:
    print("Seu alistamento é esse ano.")
else:
    print(f"Você ainda é de menor.")
    if 18 - ano == 1:
        print(f"Ainda falta {18-ano} ano pra você se alistar.")
    else:
        print(f"Ainda faltam {18-ano} anos pra você se alistar.")
    