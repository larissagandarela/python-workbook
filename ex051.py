a1 = int(input('Digite o primeiro termo dessa PA: '))
r = int(input('Digite a razão dessa PA: '))
a10 = a1 + 9*r
for c in range(a1, a10, r):
    print('{} ' .format(c), end=' -> ')
print('ACABOU!!!')