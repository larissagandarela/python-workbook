km = float(input('Insira a quantidade de km rodados: '))
dias = int(input('Insira a quantidades de dias com o carro: '))
print('O total de quilomêtros rodados foram de {} km em um total de {} dias.' .format(km, dias))
print('O valor final a ser pago é de R${}' .format(km*0.15 + dias*60))