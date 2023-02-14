"""
Refaça o DESAFIO 009, mostrando a TABUADA de um número
que o usuário escolher, só que agora ultilizando um laço for.

"""
print("=-"*10, "TABUADA", "=-"*10)
n = int(input("Digite um número: ")) # Usuario digita número
f = 0 # Fator inical
print(f"{n} x {f} = {n * f}") # primeira multiplicação, * 0
for c in range(0, 10):
    f += 1
    print(f"{n} x {f} = {n * f}")
