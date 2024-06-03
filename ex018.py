import math
ang = float(input('Digite o ângulo desejado: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O ângulo de {}° tem o seno de {:.2f}' .format(ang, sen))
print('O ângulo de {}° tem o cosseno de {:.2f}' .format(ang, cos))
print('O ângulo de {}° tem a tangente de {:.2f}' .format(ang, tg))