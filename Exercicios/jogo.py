from random import choice
from time import sleep


lista = (1, 2, 3, 4, 5)
valor = int(input('\033[7;30;44mEscolha um número de 1 a 5: \033[m'))
print('\033[1;31mPROCESSANDO ....\033[m')
print('-*' * 25)
sleep(4)
computador = choice(lista)

if valor == computador:
    print('\033[4;34mParabénsss, você acertou o número que eu estava pensando!!!!!!! Eu realmente pensei no número {}\033[m'.format(computador))
else:
    print('\033[1;31mVocê errrrrrouuuuuuuu!!\033[m')
    print('Eu pensei no número {} e não no número {}.'.format(computador, valor))

print('\033[4;30Fim\033[m')

