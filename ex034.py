from time import sleep
salário = float(input('Qual é o salário atual? R$'))
sleep(1)
print('O seu salário é R${}' .format(salário))
sleep(1)
print('CALCULANDO O AUMENTO...')
sleep(2)
if salário <= 1250:
    aumento = salário * 0.15
    salfinal = salário * 1.15
    print('O aumento é de {} e seu salário com aumento é de R${}' .format(aumento, salfinal))
else:
    aumento = salário * 0.10
    salfinal = salário * 1.10
    print('O aumento é de {} e seu salário com aumento é de R${}' .format(aumento, salfinal))
