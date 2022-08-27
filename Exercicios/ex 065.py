simounao = ''
numeroinput = 0
quantidade = 0
media = 0
soma = 0
maiornumero = 0
menornumero = 0
while simounao != 'N':
    numeroinput = int(input('Digite um valor: '))
    simounao = str(input('Deseja continuar?[S/N] ')).upper()
    quantidade += 1
    soma += numeroinput
    media = soma / quantidade
    if (numeroinput > maiornumero):
        maiornumero = numeroinput
        
    if (numeroinput < menornumero):
        menornumero = numeroinput
print('A média desses números é {}'.format(media))
print('O maior número é {}.'.format(maiornumero))
print('O menor número é {}.'.format(menornumero))
