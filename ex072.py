print('\n{:#^60}\n'.format(' Número por Extenso '))
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
opcao = 'S'
while opcao != str('SN'):
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            print(f'você digitou o número {numeros[num]}')
            break
        else:
            print('Tente novamente.', end='')
    opcao = str(input('Deseja continuar[S/N ou s/n]: ')).upper().strip()
    if opcao == 'N':
        break

print('Encerrando...')
