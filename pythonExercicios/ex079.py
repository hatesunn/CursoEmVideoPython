"""
Crie um programa onde um usário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitado em ordem crescente.
"""

lista = []
cont = 0
while cont != 2:
    if cont == 2:
        break
    while True:
        n = int(input("Digite um número: "))
        if n in lista:
            print("Número já foi digitado. Por favor insira outro número.")
        else:
            lista.append(n)
            break
    while True:
        cont = int(input("""
Deseja continuar?
[1] Sim
[2] Não
"""))
        if cont == 1 or cont == 2:
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")      
print(f"Os números digitados foram: {lista}")
print(f"Os valores em ordem crescente é: {sorted(lista)}")
