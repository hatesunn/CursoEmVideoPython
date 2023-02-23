"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos
"""

id = 0
mulher = 0
media = 0
homem = "Não tem homem."
# Loop para ler informações das 4 pessoas
for i in range(4):
    print(f"Digite as informações da {i+1}ª pessoa:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()
    media += idade
    if sexo == "M":
        if idade > id or id == 0 :
            id = idade
            homem = nome
    elif sexo == "F":
        if idade < 20:
            mulher += 1

print(f"""A média de idade é {media/4:.2f} anos.
     O homem mais velho é o {homem}.
     Existem {mulher} mulheres abaixo de 20 anos.""")
