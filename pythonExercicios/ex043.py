# Desenvolva uma lógica que leia o peso e altura de uma pessoa.
# Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 a 40: Obesidade
# acima de 40: Obesidade mórbida

# entrada de dados
peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura(cm): "))
alt = alt / 100
imc = peso / ((alt * alt))

# saída 
print(f"Seu IMC é de: {imc:.2f}")
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está no peso ideal.")
elif 25 < imc < 30:
    print("Você está com sobrepeso.")
elif 30 < imc < 40:
    print("Você está com obesidade.")
else:
    print("Você está com obesidade mórbida.")    