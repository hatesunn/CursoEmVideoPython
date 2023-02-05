# Exercício proposto retirado do site: https://www.pythonprogressivo.net/2018/02/Exercicios-Python-IF-ELIF-ELSE.html
#
# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

import 

letra = str(input("Digite 1 letra: ")).strip().upper()
vogal = ['A','E']
print(vogal)
if letra == vogal:
    print(f"A letra ({letra}) digitada é uma vogal.")
else:
    print(f"A letra ({letra}) digitada é uma consoante.")
