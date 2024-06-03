import random
p1 = input('Digite o nome do primeiro aluno: ')
p2 = input('Digite o nome do segundo aluno: ')
p3 = input('Digite o nome do terceiro aluno: ')
p4 = input('Digite o nome do quarto aluno: ')
lista = [p1, p2, p3, p4]
sorteio = random.choice(lista)
print('O aluno escolhido foi {}' .format(sorteio))