sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:'))
print('Sexo {} registrado com sucesso' .format(sexo))