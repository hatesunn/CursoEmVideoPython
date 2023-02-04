# nome = str(input("Qual é seu nome? "))
# if nome == 'João':
#     print("Que nome lindo vc tem.")
# else:
#     print("Seu nome é tão normal!")
# print(f"Bom dia, {nome}")

n1 = float(input("Digite a primeira note: "))
n2 = float(input("Digite a segudna nota: "))
m = (n1 + n2)/2
print(f"A sua média foi {m:.1f}")
if m >= 6.0:
    print("Sua média foi boa! Parabéns!!")
else:
    print("Sua média foi rúim! Estude mais!")
