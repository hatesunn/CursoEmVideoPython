# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule  o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.

# entrada de valores
valorCasa = float(input("Qual o valor da casa?R$ "))
salario = float(input("Qual o seu salário?R$ "))
ano = int(input("Em quantos anos ele será pago? "))
prestacao = valorCasa / (ano * 12)
trinta = (salario * 30) / 100

# Saída de dados
print("\n"
    f"O valor da casa é: R$ {valorCasa:.2f}\n"
    f"O valor do seu salário é: R$ {salario:.2f}\n"
    f"A quantidade de parcelas é: {ano * 12} meses\n"
    f"O valor de cada parcela é: R$ {prestacao:.2f}\n")

# Cálculo de aprovação de crédito
if prestacao > trinta:
    print("\033[31mEmpréstimo negado!\033[m Renda abaixo do permitido.")
else:
    print("\033[32mEmpréstimo concedido\033[m.")
