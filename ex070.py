total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    total += preço
    cont += 1
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}' .format('FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos um total de {totmil} qie custa R$1000.')
print(f'O produto mais barato foi {barato} custa R${menor:.2f}')