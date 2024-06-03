def escreva(mensagem):
    print(f'{(len(mensagem) + 2) * "~"}')
    print(f' {mensagem}')
    print(f'{(len(mensagem) + 2) * "~"}')


mensagem = str(input('Digite a mensagem: '))
escreva(mensagem)