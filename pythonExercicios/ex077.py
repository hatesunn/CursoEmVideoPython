"""
Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
"""

palavras = ("aprender", "Programar", "Linguagem","Python")
print(palavras)
for palavras in palavras:
    m = palavras.upper()
    v = " "
    for l in palavras:
        if l in 'aeiou':
            v += l
    print(f"Vogais em {m}: {v}")