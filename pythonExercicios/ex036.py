# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule  o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.

# entrada de valores
valorCasa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
ano = int(input("Em quantos anos ele será pago? "))
meses = ano * 12
prestacao = valorCasa / meses
trinta = (salario * 30) / 100

# Saída de dados
print(" ")
print(f"O valor da casa é: R$ {valorCasa:.2f}")
print(f"O valor do seu salário é: R$ {salario:.2f}")
print(f"A quantidade de parcelas é: {meses} meses")
print(f"O valor de cada parcela é: R$ {prestacao:.2f}\n")

# Cálculo de aprovação de crédito
# print(prestacao, trinta)
if prestacao > trinta:
    print("\033[31mEmpréstimo negado!\033[m Renda abaixo do permitido.")
else:
    print("\033[32mEmpréstimo concedido\033[m.")
