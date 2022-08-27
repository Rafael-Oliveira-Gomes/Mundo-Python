from random import choice
from time import sleep
num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
aleatorio = choice(num)
escolha = int(input('Sou seu computador...Em que número eu estou pensando? Escolha de 1 a 10: '))
print('\033[1;35mPROCESSANDO...\033[m')
quantida = 0
while escolha != aleatorio:
    quantida += 1
    sleep(1)

    if (escolha == aleatorio):
        print('\033[1;34mParabénss, você ganhou de mim, eu pensei no número {}.\033[m'.format(aleatorio))

    else:
        #print('\033[1;35mPROCESSANDO...\033[m')
        #sleep(1)

        print('\033[1;31mVocê errrrrrouuuuuuuu.\033[m')
        escolha = int(input('Tente novamente: '))
        if escolha < aleatorio:
            print('Mais...')
        elif escolha > aleatorio:
            print('Menos...')
print('\033[1;34mVOCÊ GANHOU DE MIM\033[m')
print('Depois de {} tentativas.'.format(quantida))

