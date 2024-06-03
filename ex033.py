a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    menor = b
if c > a and c > b:
    menor = c
print('O menor número é {} e o maior é {}.'.format(menor, maior))
