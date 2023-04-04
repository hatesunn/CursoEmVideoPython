"""
Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem
por extenso. de zero até vinte.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.
"""

n = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", 
     "Onze", "Doze", "Treze", "Quartoze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
l = 0
while l in (0,20):
    l = int(input("Digite um número: "))
print(n[l])