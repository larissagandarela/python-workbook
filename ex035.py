a = float(input('Primeiro lado do triângulo: '))
b = float(input('Segundo lado do triângulo: '))
c = float(input('Terceiro lado do triângulo: '))
if a < b + c and b < a + c and c < b + a:
    print('Então temos um triângulo.')
else:
    print('As medidas fornecidas não podem formar um triângulo.')