from time import sleep
distancia = float(input('Digite a distância em quilômetros que será percorrida: '))
print('Você percorrerá {} km.' .format(distancia))
sleep(1)
print('CALCULANDO O VALOR QUE SERÁ PAGO...')
sleep(3)
if distancia > 200:
    valor = distancia * 0.45
    print('O valor total que deverá ser pago é de R${}.' .format(valor))
else:
    valor = distancia * 0.5
    print('O valor total que deverá ser pago é de R${}' .format(valor))



