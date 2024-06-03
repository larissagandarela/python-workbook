num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
num3 = int(input('Informe o terceiro valor: '))
num4 = int(input('Informe o quarto valor: '))
tup = (num1, num2, num3, num4)
con = int(input('Informe qual valor você gostaria de contar: '))
ps = int(input('Informe qual valor gostaria de encontrar a posição: '))
print(f'O numero {con} aparece {tup.count(con)} vezes')
if (tup.count(ps) == 0):
    print(f'O valor {ps} não foi encontrado em nenhuma posição')
else:
    print(f'O numero {ps} está na {tup.index(ps)+1}ª posição')
guarde = []
for p in tup:
    if (p % 2 == 0):
        guarde.append(p)
if (len(guarde) > 0):
    print(f'Os numeros pares são: ', end='')
    for g in sorted(set(guarde)):
        print(f'{g}', end=' ')
else:
    print('Não foram inseridos numeros pares!')