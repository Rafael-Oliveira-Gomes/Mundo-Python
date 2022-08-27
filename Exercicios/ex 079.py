lista = []
continuar = ''
copia = []
while continuar != 'N':
    valorinput = (int(input('Digite um valor: ')))
    lista.append(valorinput)

    if valorinput in copia:
        print('Esse valor já está na lista e não será adicionado.')
        lista.pop()
    continuar = (str(input('Quer continuar? [S/N] '))).upper()
    copia = lista[:]
    
print('Os valores digitados foram : {}'.format(sorted(lista)))
