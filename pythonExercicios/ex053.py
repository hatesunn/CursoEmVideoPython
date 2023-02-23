"""
Crie um programa que leia uma FRASE qualquer e diga se ela é um
PALÍNDROMO, desconsiderando os espaços.
"""

f = str(input("Digite uma frase: ")).strip().upper()
palavra = f.split()
junto = "".join(palavra)
inverso = ""
for letra in range(len(junto)-1, -1,-1):
    inverso += junto[letra]
print(f"O inverso de {f} é {inverso}")
if inverso == junto:
    print("É um palíndromo!")
else:
    print("Não é palíndromo!")
