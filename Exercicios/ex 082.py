lista = []
par = []
impar = []
continuar = ''
while True:
    valorinput = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    lista.append(valorinput)
    if valorinput % 2 == 0:
        par.append(valorinput)
    else:
        impar.append(valorinput)
    if continuar == 'N':
        break
print('Todos os valores digitados foram: {}'.format(lista))
print('Todos os pares digitados foram: {}'.format(par))
print('Todos os ímpares digitados foram: {}'.format(impar))
 