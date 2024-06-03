from datetime import date
ano = int(input('Qual foi o ano em que você nasceu? '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('Você tem {} anos. Sua classificação é MIRIM!!!' .format(idade))
elif 9 < idade <= 14:
    print('Você tem {} anos. Sua classificação é INFANTIL!!!'.format(idade))
elif 14 < idade <= 19:
    print('Você tem {} anos. Sua classificação é JÚNIOR!!!'.format(idade))
elif 14 < idade <= 25:
    print('Você tem {} anos. Sua classificação é SÊNIOR!!!'.format(idade))
else:
    print('Você tem {} anos. Sua classificação é MASTER!!!'.format(idade))