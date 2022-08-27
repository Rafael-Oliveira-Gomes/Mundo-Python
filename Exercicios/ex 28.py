from random import choice
from time import sleep #faz o programa esperar
numero = ('1', '2', '3', '4', '5', '0')
num = choice(numero)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivilhar...')
print('-=-' * 20)
escolha = (input('Em que número eu pensei: '))
print('Processando...')
sleep(2)
if escolha == num:
    print('Parabéns, você acertou, eu pensei no número {}'.format(num))
else:
    print('Não foi dessa vez, eu pensei no número {} e não no {}'.format(num, escolha))



