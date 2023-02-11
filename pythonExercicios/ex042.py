# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

# entrada de dados
a = float(input("Digite o tamanho do lado a: "))
b = float(input("Digite o tamanho do lado b: "))
c = float(input("Digite o tamanho do lado c: "))

if a + b > c and b + c > a and c + a > b:
    print("Forma-se um triângulo.")
    if a == b == c:
        print("Esse triângulo possui todos os lados iguais. É um Equilátero.")
    elif a != b != c != a:
        print("Esse triângulo possui 2 lados iguais. É um Escaleno.")
    else:
        print("Esse triângulo possui todos os lados diferentes. É um Isóceles.")
else:
    print("Não forma um triângulo.")
