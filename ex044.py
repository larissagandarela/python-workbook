from time import sleep
print('{:=^40}' .format(' LOJAS GANDARELA '))
sleep(1)
preço = float(input('Qual é o valor do preço de compras? R$'))
sleep(1)
print('''Escolha uma forma de pagamento
[ 1 ] À vista no cartão;
[ 2 ] 2x no cartão;
[ 3 ] 3x no cartão;
[ 4 ] À vista/Cheque.''')
opção = int(input('Sua opção: '))
if opção == 1:
    desconto = 0.05*preço
    p1 = 0.95*preço
    sleep(1)
    print('CALCULANDO O DESCONTO...')
    sleep(2)
    print('O seu produto que custa R${}, o desconto de 5% é de R${}.' .format(preço,desconto))
    sleep(1)
    print('CALCULANDO O NOVO VALOR...')
    sleep(2)
    print('O produto passa a curtar R${}' .format(p1))
elif opção == 2:
    sleep(1)
    print('Para essa modalidade não tem desconto disponivel...')
    print('O seu produto custa R${}. Em duas prestações iguais e sem juros de R${}.' .format(preço, preço/2))
elif opção == 3:
    desconto = 0.2 * preço
    p3 = 1.2 * preço
    sleep(1)
    print('CALCULANDO O DESCONTO...')
    sleep(2)
    print('O seu produto que custa R${}, o acréscimo de 20% é de R${}.'.format(preço, desconto))
    sleep(1)
    print('CALCULANDO O NOVO VALOR...')
    sleep(2)
    print('O produto passa a custar R${}. Em três prestações iguais de R${}.'.format(p3,p3/3))
elif opção == 4:
    desconto = 0.1 * preço
    p1 = 0.9 * preço
    sleep(1)
    print('CALCULANDO O DESCONTO...')
    sleep(2)
    print('O seu produto que custa R${}, o desconto de 10% é de R${}.'.format(preço, desconto))
    sleep(1)
    print('CALCULANDO O NOVO VALOR...')
    sleep(2)
    print('O produto passa custar R${}'.format(p1))

