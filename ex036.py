from time import sleep
salario = float(input('Qual é o valor do seu salário atual? R$'))
casa = float(input('Qual é o valor da casa que você deseja comprar? R$'))
anos = int(input('Em quantos anos você que pagar essa casa? '))
sleep(1)
print('O valor do seu salário é de R${} e você deseja um empréstimo no valor de R${} para pagar no tempo de {} anos.' .format(salario,casa, anos))
sleep(1)
meses = anos*12
valorprest = casa/meses
print('CALCULANDO O VALOR DE SUAS PRESTAÇÕES...')
sleep(2)
print('O valor de suas prestações ficará por R${:.2f}' .format(valorprest))
sleep(1)
print('ANALISANDO O SEU EMPRÉSTIMO...')
sleep(3)
if valorprest <= 0.3*salario:
    print('Parabéns seu empréstimo foi concedido!!!!!!')
else:
    print('Infelizmente seu empréstimo não foi concedido.')
