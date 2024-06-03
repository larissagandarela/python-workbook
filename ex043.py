peso = float(input('Qual é o seu peso em Kg? '))
altura = float(input('Qual é a sua altura em metros? '))
imc = peso/(altura**2)
print('Seu IMC é de {:.1f}' . format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!!!')
elif 18.5 <= imc < 25:
    print('Você está com o peso IDEAL!!!!')
elif 25 <= imc < 30:
    print('Você está com sobrepreso!!!!')
elif 30 <= imc < 40:
    print('Você está OBESO!!!!')
else:
    print('Você está em OBESIDADE MORBIDA!!!!')
