número = list()
pares = list()
ímpares = list()
while True:
    número.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(número):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-'*60)
print(f'A lista completa é {número}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
