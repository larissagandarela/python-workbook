print('=' * 40)
print(f'{"Área do Terreno":^40}')
print('=' * 40)


def area(l, c):
    a = l * c
    print(f'O seu terreno de {l}x{c} tem uma área de {a:.1f}m².')


l = float(input('Digite a largura do terreno (m): '))
c = float(input('Digite o comprimento do terreno (m): '))
area(l, c)

