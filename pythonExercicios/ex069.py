"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""

maioridade = h = m = 0
cont = "S"
while True:
    idade = int(input("Digite idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Digite sexo(M/F): ")).strip().upper()[0]
    if idade > 18:
        maioridade += 1
    if sexo  == "M":
        h += 1
    if sexo == "F" and idade < 20:
        m += 1
    cont = input("Deseja continuar(S/N)? ").strip().upper()[0]
    while cont not in "SN":
        cont = input("Deseja continuar(S/N)? ").strip().upper()[0]
    if cont == "N":
        break
print(f"Teve {maioridade} maiores de idade, {h} homens e {m} mulheres com menos que 20 anos.")