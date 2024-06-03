from time import sleep
velocidade = float(input('Qual velocidade você estava dirigindo? '))
if velocidade > 80:
    print('Você execedeu o limite de velocidade!!!!! Você será multado!!')
    multa = (velocidade - 80) * 7
    print('CALCULANDO A MULTA...')
    sleep(2)
    print('Você deve pagar uma multa de {:.2f}!' .format(multa))
print('Você está no limite de velocidade. Dirija com segurança!!!!!')