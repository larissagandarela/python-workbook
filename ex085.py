lista = [[], []]
for c in range(1, 8):
    n = int(input(f'Informe o {c}° Valor:  '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('-=' * 15)
lista[0].sort()
lista[1].sort()
print(f'Os PARES são: {sorted(lista[0])}')
print(f'Os ÍMPARES  são: {sorted(lista[1])}')
