#Mensagem de erro

sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input(' Tente novamente: ')).strip().upper()[0]
    if (sexo != 'M') and (sexo !='F'):

        print('\033[1;31mDADOS INVÁLIDOS.\033[m')
print('Sexo registrado com sucesso.')