"""
Melhore o ex061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos
"""

print("-="*10,"Progressão Aritmética","-="*10)

a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
a10 = 0
termos = 10
while a10 < 10:
   print (a1, end="-> ")
   a1 = a1 + r
   a10 += 1
print("Acabou")
cont = 1
while cont != 0:
    cont = int(input("Mais quantos termos deseja(0 para sair)? "))
    if cont == 0:
        print("Saindo...")
    else:
        a10 = 0
        termos += cont
        while a10 < cont:
            print (a1, end="-> ")
            a1 = a1 + r
            a10 += 1
        print("Acabou")
print(f"Você saiu com {termos} termos mostrados.")