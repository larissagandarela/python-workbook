import random
from random import randint
from time import sleep


def validar_sorteio(jogadores, embaralhados):
    for i in range(len(participantes)):
        if participantes[i] == embaralhados[i]:
            return False
        return True


n = int(input('digite o número de participantes: '))
participantes = []


for i in range(n):
    nome = input('Digite o nome do {}º participantes: '.format(i+1))
    participantes.append(nome)

embaralhados = random.sample(participantes, len(participantes))
while not validar_sorteio(participantes, embaralhados):
    embaralhados = random.sample(participantes, len(participantes))

print("Resultado do sorteio: ")
for i in range(len(participantes)):
    print(participantes[i], 'tirou', embaralhados[i])
    print('{} tirou {}'.format(participantes[i], embaralhados[i]))