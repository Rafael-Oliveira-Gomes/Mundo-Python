continuar = ''
dicionario = {}
listaPesssoas = []
cont = 0
media = 0
listaMulheres = []
while continuar != 'N':
    #cadastro
    nomeInput = str(input('Nome: '))
    sexoInput = str(input('Sexo: [M/F]')).upper()
    idadeInput = int(input('Idade: '))
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    cont += 1
    media = (media + idadeInput) / cont
    #dicionario
    dicionario[nomeInput] = nomeInput
    dicionario[sexoInput] = sexoInput
    dicionario[idadeInput] = idadeInput
    #lista
    listaPesssoas.append(dicionario[nomeInput])
    listaPesssoas.append(dicionario[sexoInput])
    listaPesssoas.append(dicionario[idadeInput])
    #lista de mulheres
    if 'F' in sexoInput:
        listaMulheres.append(nomeInput)



print('No total foram {} pessoas cadastradas.'.format(cont))
print('A média de idade desse grupo é {}'.format(media))
print('A lista com todas as mulheres do grupo é: {}'.format(listaMulheres))
