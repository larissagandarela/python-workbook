import math
cat1 = float(input('Qual é a medida do primeiro cateto? '))
cat2 = float(input('Qual é a medida do segundo cateto? '))
hip = math.hypot(cat1, cat2)
print('A hipotenusa vai medir {:.2f}' .format(hip))