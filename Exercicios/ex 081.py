lista = []
continuar = ''
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar in 'Nn':
        break
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista') 
listaAOcontrario = lista.sort(reverse=True)
print('Foram digitados {} números.'.format(len(lista)))
print('Na ordem decrescente fica {}'.format(listaAOcontrario))
