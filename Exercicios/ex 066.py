soma = 0
contador = 0
while True:
    numeroinput = int(input('Digite um valor (999 para parar): '))
    if numeroinput == 999:
        break
    soma += numeroinput
    contador += 1
print('A soma desses {} números é {}.'.format(contador, soma))
