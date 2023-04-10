valores = []
p = 0
for x in range(3):
    valores.append(p)
    p += 1
for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Cheguei ao final da lista.")
