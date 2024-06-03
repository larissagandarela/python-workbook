dados = dict()
jogos = list()
jogador = str(input('Digite o nome do jogador: '))
n = int(input('Quantas partidas o {} jogou??? '.format(jogador)))
s = 0
for c in range(1, n+1):
  j = int(input(' Quantos gols ele marcou no {}º jogo? '.format(c)))
  s += j
  jogos.append(j)
dados['Jogador:'] = jogador
dados['Gols'] = jogos
dados['Total:'] = s
print('-'*15)
print(dados)
print('-'*15)
for k,v in dados.items():
  print('O campo {} tem o valor de {} \n'.format(k, v))
print('-'*20)
print('O jogador {} jogou {} partidas'.format(jogador, n))
for p in range(1, n+1):
    print('  => Na partida {} marcou {} golos.\n'.format(p, jogos[p-1]))
print('-'*20)