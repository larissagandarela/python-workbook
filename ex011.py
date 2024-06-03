lar = float(input('Qual é o comprimento da parede?'))
alt = float(input('Qual é a altura da parede?'))
print('A parede tem a dimensão de {}x{}, a sua área é de {} m²' .format(lar, alt, lar*alt))
print('Para pintar essa parede você precisará de {:.2} litros de tinta' .format((lar*alt)/2))