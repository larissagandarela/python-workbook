from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('=' * 30)
print('Jogador jogou {}'.format(itens[jogador]))
print('O computador escolheu {}.' .format(itens[computador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE!!')
    elif jogador == 1:
        print('JOGADOR VENCE!!!')
    elif jogdor == 2:
        print('O COMPUTADOR VENCE!!!')
    else:
        print('Jogada inválida!!!!')
elif computador == 1:
    if jogador == 0:
        print('O COMPUTADOR VENCE!!!')
    elif jogador == 1:
        print('EMPATE!!')
    elif jogdor == 2:
        print('JOGADOR VENCE!!!')
    else:
        print('Jogada inválida!!!!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!!!')
    elif jogador == 1:
        print('O COMPUTADOR VENCE!!!')
    elif jogdor == 2:
        print('EMPATE!!')
    else:
        print('Jogada inválida!!!!')
