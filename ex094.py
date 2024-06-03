dados = dict()
pessoas = list()
tot = media = 0
while True:
    dados['nome'] = str(input('Nome: ')).strip().title()
    sexo = str(input('Sexo: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('F(feminino) M(masculino): ')).strip().upper()[0]
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('S(continuar) N(terminar): ')).strip().upper()[0]
    if res == 'N':
        break
print('-' * 30)
# A) Quantas pessoas foram cadastradas
if len(pessoas) == 1:
    print(f'O grupo tem {len(pessoas)} pessoa.')
else:
    print(f'O grupo tem {len(pessoas)} pessoas.')
#  B) A MÉDIA de idade do grupo
for p, d in enumerate(pessoas):
    for idade in d.values():
       if idade == d['idade']:
           tot += idade
media = tot / len(pessoas)
print(f'Média de idade é de {media:.2f} anos.')
# C) Uma lista com todas as mulheres
print('Mulheres cadastradas foram: ',end='')
for p, d in enumerate(pessoas):
    for mulher in d.values():
        if d['sexo'] == 'F':
            print(d["nome"], end=' ')
            break
# D) Uma lista com todas as pessoas com IDADE acima da MÉDIA
print('\nPessoas acima da média: ')
for p, d in enumerate(pessoas):
    for acima in d.values():
        if d['idade'] > media:
            print(f'\t{d["nome"]} do sexo {d["sexo"]} com {d["idade"]} anos')
            break

print('ENCERRADO!!!!!')