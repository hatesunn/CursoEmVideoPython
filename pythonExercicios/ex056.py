"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos
"""
mIdade = 0
m20 = 0
velho = "Ninguém"
for d in range(0,4):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Sexo(M= Masculino e F= Feminino): ")
    mIdade += idade
    if sexo == "F" and idade < 20:
        m20 += 1
    if sexo == "M"
    
        
