# Crie um jogo que jogue vs cpu Jokenpô

# import random e loading
from random import randint 
from time import sleep 

cpu = randint(0, 2) # escolhas do cpu

# apresentação
print("-=-" * 20)
print("Vamos jogar Jokenpô. Escolha Papel, Pedra ou Tesoura:\n"
        "[0]Papel\n"
        "[1]Pedra\n"
        "[2]Tesoura")
jogador = int(input(""))

# travar numero errado
while jogador > 2:
    jogador = int(input("Escolha inválida. Escolha Papel, Pedra ou Tesoura:\n"
        "[0]Papel\n"
        "[1]Pedra\n"
        "[2]Tesoura\n"))

# loading
print("Processando...")
sleep(1.3)

# escolhas do jogador
if jogador == 0:
    jog = "Papel"
elif jogador == 1:
    jog = "Pedra"
elif jogador == 2:
    jog = "Tesoura"
# escolhas cpu
if cpu == 0:
    cp = "Papel"
elif cpu == 1:
    cp = "Pedra"
elif cpu == 2:
    cp = "Tesoura"

# saída
print(f"Você escolheu {jog} e eu escolhi {cp}")
if jogador == cpu:
    print("Empatou")
elif (jogador == 0 and cpu == 2) or (jogador == 1 and cpu == 0) or (jogador == 2 and cpu == 1):
    print("Ganhei. Mais sorte na próxima vez!")
elif (jogador == 0 and cpu == 1) or (jogador == 1 and cpu == 2) or (jogador == 2 and cpu == 0):
    print("Parabéns, você venceu!")
    
print("-=-" * 20)
