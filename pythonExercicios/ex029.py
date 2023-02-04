# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80kmh, mostre uma mensagem dizendo
# que ele foi multado
# A multa vai custar 7,00 por cada km acima do limite

vel = int(input("Digite o valor da velocidade (em km): "))
multa = float((vel - 80) * 7)
if vel > 80:
    print(f"Sua velocidade é: {vel} km/h, você excedeu o limite de velocidade e receberá um multa de: R$ {multa:.2f}.")
else:
    print(f"Sua velocidade é: {vel} km/h. Parabéns! Você está dentro do limite.")
