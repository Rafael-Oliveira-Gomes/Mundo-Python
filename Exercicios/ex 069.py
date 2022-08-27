contadoridade = 0
contadorhomem = 0
contadormulher = 0

while True:
    print('-'*15)
    print('   CADASTRE UMA PESSOA')
    idadeinput = int(input('Idade: '))
    sexoinput = str(input('Sexo: [M/F] ')).upper()
    print('-' *15)
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if idadeinput >= 18:
        contadoridade += 1
    if (sexoinput in 'M'):
        contadorhomem += 1
    if (idadeinput >= 20) and (sexoinput in 'F'):
        contadormulher += 1
    if continuar in 'N':
        break

print('O total de pessoas maiores de 18 anos é {}.'.format(contadoridade))
print('O total de homens cadastrados foi {}.'.format(contadorhomem))
print('O total de mulheres com menos de 20 anos é {}.'.format(contadormulher))
print('-'*15)
print('FIM DO PROGRAMA')
print('-'*15)
