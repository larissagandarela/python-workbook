import random


lista = []
for p in range (0,5):
    lista.append(str(input(f'Digite um valor para a Posição {p}: ')))
    random.shuffle(lista)
print(lista)




