"""
Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
"""

palavras = ("aprender", "Programar", "Linguagem","Python")
print(palavras)
for palavras in palavras:
    print(f"\nVogais em {palavras.upper()}: ", end="")
    for l in palavras:
        if l.lower() in 'aeiou':
            print(l, end=" ")