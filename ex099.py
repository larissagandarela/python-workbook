from time import sleep

def maior(* numero):
    cont = maior = 0
    print('-' * 60)
    print('Analisando os valores passados...')
    for valor in numero:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 8, 6, 3, 1)
maior(4, 7, 0)
maior(1, 2)
maior(0)
maior()