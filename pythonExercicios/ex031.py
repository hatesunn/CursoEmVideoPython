# Desenvolva um programa que pergunte a distância de uma viagem
# em KM. Calcule o preço da passagem, cobrando 0.50 por km
# para viagens de até 200km e 0.45 para viagens mais longas

dist = int(input("Digite a distância da viagem (em km): "))
if dist <= 200:
    print(f"O valor da passagem é R$ {dist * 0.50:.2f}")
else:
    print(f"O valor da passagem é R$ {dist * 0.45:.2f}")
