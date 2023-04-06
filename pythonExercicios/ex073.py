"""
Crie uma tupla preenchida com os 20 primeiros colocados da tablea do CB, na ordem de colocação. Depois mostre:
A) Apenas o 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times eme ordem alfabética.
D) Em que posicão na tabela está o time SP.
"""

times = (
"Palmeiras",
"Internacional",
"Fluminense",
"Corinthians",
"Flamengo",
"Athletico-PR",
"Atletico-MG",
"Fortaleza",
"Sao Paulo",
"America-MG",
"Botafogo",
"Santos",
"Goias",
"Bragantino",
"Coritiba",
"Cuiaba",
"Ceara-SC",
"Atletico-GO",
"Avai",
"Juventude"
)
print("\n{:=^140}".format(" \033[032mTimes do Brasileirão Série A\033[m "))
print(times)
print("{:=^140}".format(" \033[032mOs 5 primeiros times\033[m "))
print(times[:5])
print("{:=^140}".format(" \033[032mOs 4 na zona de rebaixamento\033[m "))
print(times[-4:])
print("{:=^140}".format(" \033[032mOrdem alfabética\033[m "))
print(sorted(times))
print("{:=^140}".format(" \033[032mO Sao Paulo está na posição\033[m "))
print(times.index("Sao Paulo")+ 1,"ª posição")
print("{:=^140}".format(" \033[032m Fim do programa \033[m "))