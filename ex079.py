números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado!!! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print('-'*60)
números.sort()
print(f'Você digitou os valores {números}')
