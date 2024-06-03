from time import sleep
from random import  randint
computador = randint(0, 10) #faz o computador pensar
print('-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-' *20)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('PARABÉNS, VOCÊ CONSEGUIU ME VENCER com {} tentativas!!'.format(palpite))
