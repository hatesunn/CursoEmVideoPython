# Exercício proposto retirado do site: https://www.pythonprogressivo.net/2018/02/Exercicios-Python-IF-ELIF-ELSE.html
#
#  Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:
""""
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez. """

nota1 = float(input("Digite a nota do primeiro semestre: "))
nota2 = float(input("Digite a nota do segundo semestre: "))
final = (nota1 + nota2) / 2
if final == 10:
    print(f"Sua nota final foi {final:.2f}. Parabéns você foi\033[32m aprovado \033[mcom nota máxima!")
elif final >= 7:
    print(f"Sua nota final foi {final:.2f}. Você foi\033[34m aprovado\033[m!")
else:
    print(f"Sua nota final foi {final:.2f}. Você foi\033[31m reprovado\033[m!")
