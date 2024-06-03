a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
if a < b:
    maior = b
    print(' Entre {} e {} o maior é {}.'.format(a, b, maior))
elif a > b:
    maior = a
    print(' Entre {} e {} o maior é {}.' .format(a,b, maior))
else:
    print('Esse números são iguais!!!')
