a = float(input('Primeiro lado do triângulo: '))
b = float(input('Segundo lado do triângulo: '))
c = float(input('Terceiro lado do triângulo: '))
if a < b + c and b < a + c and c < b + a:
    print('Os lados acima forma um triângulo!!',   end='\n')
    if a == b == c:
        print('É um triângulo EQUILÁTERO!!!!')
    elif a == b and a != c:
        print('É um triângulo ISÓCELES!!!')
    else:
        print('É um triângulo ESCALENO!!!!')
else:
    print('Os lados acima não forma um triângulo!!')

