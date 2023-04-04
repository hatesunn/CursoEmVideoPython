"""
Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem
por extenso. de zero até vinte.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.
"""

n = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", 
     "Onze", "Doze", "Treze", "Quartoze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
while True:
    l = int(input("Digite um número: "))
    if 0 <= l <= 20:
        break
print(n[l])
print("Finalizando...")