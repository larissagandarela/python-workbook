n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
média = (n1 + n2)/2
if média < 5:
    print('Sua média foi {}. Você está REPROVADO!!!!!' .format(média))
elif 5 <= média <= 6.9:
    print('Sua média foi {}. Você está de RECUPERAÇÃO!!!!!' .format(média))
else:
    print('Sua média foi {}. Você está APROVADO!!!!!!' .format(média))