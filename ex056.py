somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
for pessoas in range(1, 5):
    print('---- {}ª PESSOA ----'.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorodadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade | 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print("Ao todo são {} mulheres com medo de 20 anos.".format(totmulher20))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem))
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
