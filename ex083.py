lista1 = []
lista2 = []
e = input('Expressão: ')
for c in e:
    if c == '(':
        lista1.append(c)
    elif c == ')':
        lista2.append(c)
if len(lista1) == len(lista2):
    print('Expressão correta!!!!!')
else:
    print('Expressão errada!!!!!')