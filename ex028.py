from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador pensar
print('-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-' *20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS, VOCÊ CONSEGUIU ME VENCER!!!!!!!!')
else:
    print('GANHEI!!!! Eu pensei no número {} e não no {}!' .format(computador, jogador))

