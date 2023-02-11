# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final
# de acordo com a média atingida:
# média abaixo de 5.0: reprovado
# média entra 5.0 e 6.9: Recuperação
# média acima de 7.0: aprovado

# leitura de dados
nota1 = float(input("Digite sua nota do primeiro semestre: "))
nota2 = float(input("Digite sua nota do segundo semestre: "))
media = (nota1 + nota2) / 2

if media < 5:
    print(f"Sua média final é {media:.2f}. \033[31mVocê está reprovado!\033[m")
elif 7 > media >= 5:
    print(f"Sua média final é {media:.2f}. \033[33mVocê está de recuperação!\033[m")
else:
    print(f"Sua média final é {media:.2f}. \033[32mVocê está aprovado!\033[m")
