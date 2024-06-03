from datetime import date
nas = int(input("Qual é o ano que você nasceu? "))
ano = date.today().year
idade: idade = ano - nas
print('Você nasceu {} e tem {} anos.' .format(nas,idade))
if idade < 18:
    print('Você não pode se alistar!!!! Faltam {} anos.'.format(18 - idade))
elif idade > 18:
    print('Você precisa se alistar!!! Já se passaram {} anos.' .format(idade-18))
else:
    print('Esse será seu ano de alistamento!!!')
