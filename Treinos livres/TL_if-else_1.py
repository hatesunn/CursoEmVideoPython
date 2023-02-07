# Exercício proposto retirado do site: https://www.pythonprogressivo.net/2018/02/Exercicios-Python-IF-ELIF-ELSE.html
#
# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite 1 letra: ")).strip().upper()
# if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
if letra in 'A E I O U':
    print(f"A letra ({letra}) digitada é uma vogal.")
else:
    print(f"A letra ({letra}) digitada é uma consoante.")
