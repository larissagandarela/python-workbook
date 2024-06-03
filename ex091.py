import random
from time import sleep

jogadores = {input(f'\nNome das pessoas {i}: ').capitalize(): random.randint(1, 5) for i in range(1, 6)}


for k, v in jogadores.items():
    sleep(1), print(f'\n{k} tirou.'), sleep(1)
    if v == 1:
        print('item 1')
    elif v == 2:
        print('item 2')
    elif v == 3:
        print('item 3')
    else:
        print('item 4')

