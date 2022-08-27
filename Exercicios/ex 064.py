numeroinput = 0
soma = 0
quantidade = 0
while numeroinput != 999:
    numeroinput = int(input('Digite um número: '))
    quantidade += 1
    soma += numeroinput 
    
print('O total de números digitados foi {}.'.format(quantidade - 1))
print('E a soma deles é {}.'.format(soma - 999))
