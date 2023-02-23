"""
Refaça o DESAFIO 009, mostrando a TABUADA de um número
que o usuário escolher, só que agora ultilizando um laço for.

"""

print("=-"*10, "TABUADA", "=-"*10)
n = int(input("Digite um número: ")) # Usuario digita número
for c in range(1, 11):
    print(f"{n} x {c:2} = {n * c}")
