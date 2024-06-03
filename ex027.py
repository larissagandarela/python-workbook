n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!!!!')
print('Seu primeiro nome é {} e o seu último nome é {}.' .format(nome[0], nome[len(nome)-1]))