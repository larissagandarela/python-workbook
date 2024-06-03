ficha = {}
lista = []
from datetime import datetime
while True:
    ficha["Nome"] = str(input('Nome: ')).strip().capitalize()
    ficha["Nasc"] = int(input('Ano de nasc.: '))
    ficha["CTPS"] = int(input('Núm. CTPS (Digite 0 se não tiver carteira): '))
    if ficha["CTPS"] != 0:
        ano = int(input('Ano contratação: '))
        sal = float(input('Salário: R$'))
        ficha["Apo"] = 35 - (datetime.now().year-ano)
        lista += [ficha.copy()]
    flag = str(input('Continuar? (S/N) ')).strip().lower()
    if flag == 'n':
       break
for x in range(0, len(lista)):
    print('='*20, end='')
    print(f'\nNome: {lista[x]["Nome"]}. '
          f'\nIdade: {2019-(lista[x]["Nasc"])}. '
          f'\nCarteira de trabalho: {lista[x]["CTPS"]}.'
          f'\nAposentadoria em {lista[x]["Apo"]} anos.')